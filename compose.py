import os
import shutil
import subprocess

from .constants import COMPOSEDIR_TEMPLATE, WSGI_APP_DIR, CONFIGS_DIR, NGINX_CONF_DIR, REQUIREMENTS_NAME,
    DOCKERFILE, DOCKER_COMPOSE, GUNICORN_START, DEFAULT_PYTHON_VERSION, DEFAULT_SERVER_NAME,
    DEFAULT_APP_NAME, DEFAULT_NUM_WORKERS, DEFAULT_COMPOSE_DIR


def build(project_path,
          wsgi_path,
          requirements_path=None,
          python_version=DEFAULT_PYTHON_VERSION,
          server_name=DEFAULT_SERVER_NAME,
          app_name=DEFAULT_APP_NAME,
          num_workers=DEFAULT_NUM_WORKERS,
          builddir_path=DEFAULT_COMPOSE_DIR):

    try:
        os.makedirs(builddir_path)
    except OSError:
        print("ERROR: %s directory exists - EXIT" % builddir_path)
        exit()

    wsgi_app_path = os.path.join(builddir_path, WSGI_APP_DIR)
    os.makedirs(wsgi_app_dir)
    nginx_conf_dir_path = os.path.join(builddir_path, NGINX_CONF_DIR)
    os.makedirs(nginx_conf_dir_path)
    if requirements_path:
        shutil.copyfile(requirements_path, os.path.join(builddir_path, CONFIGS_DIR, REQUIREMENTS_NAME))
    else:
        open(os.path.join(builddir_path, CONFIGS_DIR, REQUIREMENTS_NAME), 'w').close()

    project_parent_path = os.path.split(project_path)[0]
    mounted_project_path = os.path.join(WSGI_APP_DIR, os.path.dirname(project_path))
    mounted_wsgi_path = wsgi_path.replace(project_path, mounted_project_path)
    
    create_nginx_conf(mounted_project_path=mounted_project_path,
                      server_name=server_name,
                      app_name=app_name,
                      template_path=os.path.join(COMPOSEDIR_TEMPLATE, NGINX_CONF_DIR, 'wsgi_app.conf'),
                      conf_path=os.path.join(builddir_path, NGINX_CONF_DIR, app_name+".conf"))
    create_start_gunicorn(mounted_wsgi_path=mounted_wsgi_path,
                          app_name=app_name,
                          num_workers=num_workers,
                          template_path=os.path.join(COMPOSEDIR_TEMPLATE, CONFIGS_DIR, GUNICORN_START),
                          create_path=os.path.join(builddir_path, CONFIGS_DIR, GUNICORN_START))
    create_dockerfile(python_version=python_version,
                      dockerfile_template_path=os.path.join(COMPOSEDIR_TEMPLATE, DOCKERFILE),
                      dockerfile_path=os.path.join(builddir_path, DOCKERFILE))
    create_compose(project_parent_path=project_parent_path,
                   builddir_path=builddir_path,
                   nginx_conf_dir_path=nginx_conf_dir_path,
                   compose_template_path=os.path.join(COMPOSEDIR_TEMPLATE, DOCKER_COMPOSE),
                   compose_path=os.path.join(builddir_path, DOCKER_COMPOSE))
    run_compose(compose_path=os.path.join(builddir_path, DOCKER_COMPOSE))


def create_nginx_conf(mounted_project_path, server_name, app_name, template_path, conf_path):
    conf_template_f = open(template_path)
    conf_f = open(conf_path, 'w')
    conf_f.write(conf_template_f.read().replace("<APP_NAME>", app_name).replace("<SERVER_NAME>", server_name).replace("<MOUNTED_PROJECT_PATH>", mounted_project_path))
    conf_f.close()
    conf_template_f.close()


def create_gunicorn_start(mounted_wsgi_path, app_name, num_workers, template_path, create_path):
    template_f = open(template_path)
    create_f = open(create_path, 'w')
    create_f.write(template_f.read().replace("<APP_NAME>", app_name).replace("<NUM_WORKERS>", num_workers).replace("<MOUNTED_WSGI_PATH>", mounted_wsgi_path))
    create_f.close()
    template_f.close()


def create_dockerfile(python_version, dockerfile_template_path, dockerfile_path):
    dockerfile_template_f = open(dockerfile_template_path)
    dockerfile_f = open(dockerfile_path, 'w')
    dockerfile_f.write(dockerfile_template_f.read().replace("<PYTHON_VERSION>", python_version))
    dockerfile_f.close()
    dockerfile_template_f.close()


def create_compose(project_parent_path, builddir_path, nginx_conf_dir_path, compose_template_path, compose_path):
    compose_template_f = open(compose_template_path)
    compose_f = open(compose_path, 'w')
    compose_f.write(compose_template_f.read().replace("</PROJECT/PARENT/PATH>", project_parent_path).replace("<BUILDDIR>", builddir_path).replace("<NGINX_CONF_DIR_PATH>", nginx_conf_dir_path))
    compose_f.close()
    compose_template_f.close()


def run_compose(compose_path):
    subprocess.call("docker-compose -f %s build" % compose_path, shell=True)
    subprocess.Popen("docker-compose -f %s up" % compose_path, shell=True)
