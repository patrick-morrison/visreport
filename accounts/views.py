from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import auth
from observations.models import Site, Observation
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('map')
        else:
             return render(request, 'accounts/login.html', {'error': "Username or password is incorrect, or user is not activated."})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': "Username has already been taken"})
            except User.DoesNotExist: 
                user = User.objects.create_user(request.POST['username'], password =request.POST['password1'], email =request.POST['email'], is_active = False)
                user.save()
                current_site=get_current_site(request)
                message=render_to_string('accounts/activate.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                }
                )
                email_message=EmailMessage(
                    'Activate your Vis.Report Account',
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
                email_message.send()
                return render(request, 'accounts/login.html', {'error': "Check your email for an activation link. This may take up to 5 minutes."})
        else:
            return render(request, 'accounts/signup.html', {'error': "Passwords must match"})
    else:
        return render(request, 'accounts/signup.html')

class ActivateAccountView(generic.View):
    def get(self, request, uidb64, token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            auth.login(request, user)
            return redirect('map')
        return render(request, 'accounts/login.html', {'error': "Could not activate, please request the activation link again."})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('map')

        
def profile(request):
    if request.method == 'POST':
        return redirect('account')
    else:
        user = request.user
        observations = Observation.objects.all().filter(user=user).order_by('-when_observed')
        return render(request, 'accounts/profile.html', {"Observations":observations})