"""
Django settings for bob_project project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Reading .env file
environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
#SECRET_KEY = 'p29vwjkkws3p4-6a*6@c@jeo&j^v%w41zw)%4_s$wv6vz)5s4o'
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # third party
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'django_tables2',
    'django_filters',
    'django_fsm',
    'django_fsm_log',
    'selenium',


    # local
    'accounts',
    'home',
    'portal',
    'interception',
    'resources',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bob_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'bob_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'proj101',
#        'USER': 'bob_user',
#        'PASSWORD': 'UPT6over!',
#        'HOST': 'localhost',
#        'PORT': '5432',
#
#    }
#}

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    #'default': env.db(),
    # read os.environ['SQLITE_URL']
    #'extra': env.db('SQLITE_URL', default='sqlite:///db.sqlite3')
    'default': env.db('SQLITE_URL', default='sqlite:///db.sqlite3')
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Custom User Settings
AUTH_USER_MODEL = 'accounts.CustomUser'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# CRISPY TEMPLATE BOOTSTRAP Version
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_CLASS_CONVERTERS = {'form-group': 'md-form'}

# Use BOOTSTRAP3 if you are using Bootstrap 3
BOOTSTRAP4 = {
    'include_jquery': True,
}

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Login url
# default: LOGIN_URL = '/accounts/login/'
LOGIN_URL = 'accounts:login' # defined by named URL pattern


# For testing. Log any emails sent to the console
# (in case of password reset, you can copy the password reset link from the website )
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATE_INPUT_FORMATS = [
    '%Y-%m-%d',
    '%m/%d/%Y',
    '%m/%d/%y',
    '%d/%m/%Y',
]


# set the django tables2 template 
DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap4.html'
