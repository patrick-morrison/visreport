
SECRET_KEY = '8(p!jvgREWYQ4SDvasdgzasDFrXZCVZXge(g(1=wdr(wmasdfasdgpksalx&2@%k43jm'

ALLOWED_HOSTS = ['128.199.208.179']


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'visreportsdb',
        'USER': 'visreporter',
        'PASSWORD': 'divesites2020',
        'HOST': "localhost",
        'PORT': 5432,
    }
}

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='vis.report.app@gmail.com'
EMAIL_HOST_PASSWORD='@6wt*cEkoco'
EMAIL_USE_TLS=True
EMAIL_PORT='587'