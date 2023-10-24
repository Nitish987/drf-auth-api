from dotenv import load_dotenv
from pathlib import Path

# Loads environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1c!e2361=wha=2pt^b0ss$^8@@8u-k6*7ds=c7o73b64wi7#!w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'account',
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

ROOT_URLCONF = 'softauth.urls'

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

WSGI_APPLICATION = 'softauth.wsgi.application'

# User Model
AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Rest API Framework configurations
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'account.authentication.UserAuthentication',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'signup': '10/min',
        'signup_verification': '100/min',
        'resent_signup_otp': '10/min',
        'login': '10/min',
        'password_recovery': '10/min',
        'password_recovery_verification': '100/min',
        'password_recovery_new_password': '10/min',
        'resent_password_recovery_otp': '10/min',
        'authenticated_user': '1000/hour',
        'change_names': '3/day',
        'logout': '10/min',
    },
    'EXCEPTION_HANDLER': 'utils.exceptions.ExceptionHandler'
}

# Jwt Config
JWT_SECRET = 'django-insecure-1c!e2361=wha=2pt^b0ss$^8@@8u-k6*7ds=c7o73b64wi7#!w'

# Softauth api key
SOFTAUTH_API_KEY = 'django-insecure-1c!e2361=wha=2pt^b0ss$^8@@8u-k6*7ds=c7o73b64wi7#!w'

# Account Creation Key
ACCOUNT_CREATION_KEY = 'django-insecure-1c!e2361=wha=2pt^b0ss$^8@@8u-k6*7ds=c7o73b64wi7#!w'

# Encryption Key
SERVER_ENC_KEY = 'django-insecure-1c!e2361=wha=2pt^b0ss$^8@@8u-k6*7ds=c7o73b64wi7#!w'

# Token expire time
SIGNUP_EXPIRE_SECONDS = 10 * 60 # 10 minute
PASSWORD_RECOVERY_EXPIRE_SECONDS = 10 * 60 # 10 minute
ONE_DAY_EXPIRE_SECONDS = 1 * 24 * 60 * 60 # 1 day
OTP_EXPIRE_SECONDS = 3 * 60 # 3 minute
RESENT_OTP_EXPIRE_SECONDS = 5 * 60 # 5 minute
PASSWORD_EXPIRE_SECONDS = 5 * 60 # 5 minute
AUTH_EXPIRE_SECONDS = 30 * 24 * 60 * 60 # 30 days


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
