"""
settings.py - Файл настроек Django

manage.py - Файл для управления проектом (создание, запуск и т.д.)

'django-admin startproject blog .' - команда для создания проекта
'blog' - название проекта (папка с проектом)

'python manage.py runserver' - команда для запуска сервера (по умолчанию на 127.0.0.1:8000)
'python manage.py runserver <port>' - команда для запуска сервера на определенном порту

'python manage.py createsuperuser' - команда для создания суперпользователя

'python manage.py migrate' - команда для применения миграций

'python manage.py startapp <app_name>' - команда для создания приложения
(app_name - название приложения, принято начинать с маленькой буквы и в единственном числе)
"""

from pathlib import Path


# BASE_DIR - переменная, содержащая путь к директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY - секретный ключ проекта
SECRET_KEY = 'django-insecure-qxoxzs729uqg^%m!w9h@$!1w8@gh)&##7cc%ysraha&5&1q6vi'

# TODO
DEBUG = True

# ALLOWED_HOSTS - список хостов, которые могут обращаться к проекту
ALLOWED_HOSTS = []


# Installed apps - список установленных приложений
INSTALLED_APPS = [
    # Приложения по умолчанию
    'django.contrib.admin', # Приложение административной панели
    'django.contrib.auth', # Приложение аутентификации пользователей
    'django.contrib.contenttypes', # Приложение для работы с контентом
    'django.contrib.sessions', # Приложение для работы с сессиями
    'django.contrib.messages', # Приложение для работы с сообщениями
    'django.contrib.staticfiles', # Приложение для работы со статическими файлами

    # my apps
    'post', # Приложение для работы с постами
]

# Middleware - список промежуточных слоев
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF - переменная, содержащая путь к корневому URL-файлу
ROOT_URLCONF = 'blog.urls'

# TEMPLATES - список шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates', # Путь к директории с шаблонами
        ],
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

# WSIG_APPLICATION - переменная, содержащая путь к WSGI-приложению
WSGI_APPLICATION = 'blog.wsgi.application'


# database - настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# AUTH_PASSWORD_VALIDATORS - список валидаторов паролей
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

# Internationalization - настройки интернационализации
LANGUAGE_CODE = 'en-us'

# TIME_ZONE - часовой пояс
TIME_ZONE = 'UTC' # +0

USE_I18N = True
USE_TZ = True

# TODO
STATIC_URL = 'static/'

# DEFAULT_AUTO_FIELD - настройка для автоматического создания первичных ключей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
