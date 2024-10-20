

from pathlib import Path
import os
import environ


env = environ.Env(
    DEBUG=(bool,False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR,".env"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-j4ippt+3h39u4ontllpc8a(4h&^god(7aicz#@q^sl_(w)2otp'
SECRET_KEY = env("SECRET_KEY",default="change_me")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG",default= False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default =["*"])

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conversation',
    'core',
    'dashboard',
    'item',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iekart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iekart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': env.db(default="sqlite:///db.sqlite3"),
}

LOGGING = {
    "version" : 1,
    "disable_existing_loggers": False,
    "handlers":{"console":{"class":"logging.StreamHandler"}},
    "loggers":{"":{"handlers":["console"],"level":"DEBUG"}},
}

SECURE_PROXY_SSL_HEADER =("HTTP_X_FORWARDED_PROTO","https")
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = env.str("STATIC_URL", default = 'static/')
MEDIA_URL = env("MEDIA_PATH",default='media/')
MEDIA_ROOT = env("MEDIA_ROOT",default = BASE_DIR / 'media')

WHITENOISE_USE_FINDER = True
WHITENOISE_AUTOREFRESH = DEBUG
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     "/var/www/static/",
# ]
STATICFILES_DIRS=[env.str("STATICFILES_DIRS", default = BASE_DIR/"static")]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = env.str("STATIC_ROOT",default= BASE_DIR/ 'staticfiles')
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'