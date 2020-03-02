"""visreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from observations import views
from observations.views import sites_view, reports_view, MapView

urlpatterns = [
    url(r'^$', MapView.as_view(), name='map'),
    path('list', views.observations_list, name = "list"),
    path('about/', views.about, name='about'),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('<str:site_code>', views.detail, name = "detail"),
    path('delete/<int:pk>', views.delete, name = "delete"),
    url(r'^sites.json/', sites_view, name='sites'),
    url(r'^reports.json/', reports_view, name='reports-json'),
]+  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
