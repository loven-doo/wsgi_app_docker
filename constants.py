import os


CONSTANTS_PATH = os.path.dirname(os.path.realpath(__file__))
COMPOSEDIR_TEMPLATE = os.path.join(CONSTANTS_PATH, 'composedir_template')
WSGI_APP_DIR = 'wsgi_app'
CONFIGS_DIR = 'configs'
NGINX_CONF_DIR = os.path.join(CONFIGS_DIR, 'nginx', 'conf.d')
REQUIREMENTS_NAME = 'requirements.txt'
GUNICORN_START = 'gunicorn_start'
DOCKERFILE = "Dockerfile'
DOCKER_COMPOSE = "docker-compose.yml"

DEFAULT_PYTHON_VERSION = '3.6'
DEFAULT_SERVER_NAME = 'localhost'
DEFAULT_APP_NAME = 'wsgi_app'
DEFAULT_NUM_WORKERS = 3
DEFAULT_COMPOSE_DIR = 'wsgi_app_composedir'
