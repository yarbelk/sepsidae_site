from os.path import abspath, basename, dirname, join, normpath
from django.contrib.messages import constants as messages
from os import environ
import sys

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
sys.path.append(DJANGO_ROOT)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dev', 'dev@mediapop.co'),
)
MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' if 'test' in sys.argv else 'django.db.backends.mysql',
        'NAME': 'sepsidae_local',
        'USER': 'sepsidae_user',
        'PASSWORD': 'hello',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

TIME_ZONE = 'Asia/Singapore'
LANGUAGE_CODE = 'en-sg'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


if 'runserver' in sys.argv:
    COMPRESS_ENABLED = True
    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
    )
else:
    COMPRESS_PRECOMPILERS = (
        # Even though we have /usr/local/bin in the PYTHONPATH it's
        # refusing to find both node and lessc. James was saying this
        # might be because it's an executed command. Even doing
        # sys.path.append('/usr/local/bin') This will be a problem
        # when someone tries to run the staging/prod settings file
        # locally on their devboxes.
        ('text/less',
         '/usr/local/bin/node '
         '/usr/local/bin/lessc --yui-compress {infile} {outfile}'),
    )

COMPRESS_DEBUG_TOGGLE = 'nocompress'
# Since we're serving from several servers
COMPRESS_CSS_HASHING_METHOD = 'content'

SECRET_KEY = r"some random key for security"

ALLOWED_HOSTS = ['.mediapop.co']

FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '%s.urls' % SITE_NAME

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'south',
    'storages',
    'bower',
    'gunicorn',
    'compressor',
    'rest_framework',
)

LOCAL_APPS = (
    'sepsid',
    'contribs',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# In Bootstrap 3 .alert-error was changed to .alert-danger.
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': [],
    },
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s %(module)s %(process)d '
                       '%(thread)d %(message)s')
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

WSGI_APPLICATION = 'wsgi.application'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_S3_SECURE_URLS = True  # All links are HTTPS
AWS_QUERYSTRING_AUTH = False

DEBUG_TOOLBAR_CONFIG = dict(
    INTERCEPT_REDIRECTS=False,
)

THUMBNAIL_QUALITY = 100
