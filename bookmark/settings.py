# Django settings for bookmark project.

import os
import socket
import getpass
import pwd

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_NAME = 'bookmark'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/bookmarks/'

# Get the current running user id
uid = getpass.getuser()

# Change this variable so that we can tell django to start/stop serving static files
SERVE_STATIC = True

# Application name
APP_NAME = 'omgmark!'

ADMINS = (
    ('Shaon Diwakar', 'shaon@shaon.net'),
)

MANAGERS = ADMINS

# We're in production and using postgres on the server
if (socket.gethostname() == 'funkhq.com' and (uid == 'funkomg')):
    print "We're in Production (Using postgres)"
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    ADMINS = (
        ('Shaon Diwakar', 'shaon@shaon.net'),
    )
    SERVE_STATIC = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME':  '<DBNAME>',   # Or path to database file if using sqlite3.
            'USER': '<USER>',                      # Not used with sqlite3.
            'PASSWORD': '<PASSWORD>',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.path.abspath(os.path.join('db')) + '/' + PROJECT_NAME + '.db',   # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-au'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.abspath(os.path.join('../assets/'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p$1nhwo50u9(o0&3sfla#n(8w!&%p50&k5r0stpqm471ixw72t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = PROJECT_NAME + '.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.abspath(os.curdir), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'registration',
    'django.contrib.messages',
    'django.contrib.admin',
    PROJECT_NAME + '.linku',
)

# 3rd party settings 
ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL = 'register@funkhq.com'

FILE_UPLOAD_MAX_MEMORY_SIZE = 512000
#FILE_UPLOAD_TEMP_DIR = os.path.abspath(os.path.join('../uploads/'))
FILE_UPLOAD_TEMP_DIR = os.path.join('../uploads/')
FILE_UPLOAD_PERMISSIONS = 0400

# Facebook application specific details
try: 
    import facebook
    FACEBOOK_API_KEY = '<FBAPIKEY>'
    FACEBOOK_APP_SECRET = '<FBAPPSEC>'
except ImportError:
    if DEBUG:
        # raise template.TemplateSyntaxError, "Error importing facebook python-sdk."
        print "Could not import facebook."
        

