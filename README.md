# Program for WSGI application Docker image creation
Creates Docker image with Nginx, Gunicorn and Postgres

## Requirements
Python >= 3.5.2  
Docker  
Docker Compose  
Python packages:  
&nbsp; - pyaml  
  
Tips for environment configuration are below

## How to use

### Install the reqirements

Required python packages can be installed after the program download (see below)  

### Download the program
To download the code type:
```
git clone https://github.com/loven-doo/wsgi_app_docker.git
```
Or you can download archive of the code via github web interface

### Install required python packages
```
pip3 install -r wsgi_app_docker/requirements.txt --upgrade
```

### Run the program
```
python3 wsgi_app_docker -pp ... -wp ... [options]
```
usage: wsgi_app_docker [-h] -pp PROJECT_PATH -wp WSGI_PATH [-sp STATIC_PATH] [-mp MEDIA_PATH]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-rp REQUIREMENTS_PATH] [-pyv PYTHON_VERSION] [-sn SERVER_NAME]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-an APP_NAME] [-nw NUM_WORKERS] [-bp BUILDDIR_PATH]  

optional arguments:  
  -h, --help            show this help message and exit  
  -pp PROJECT_PATH, --project-path PROJECT_PATH  
                        Path to the wsgi app project directory  
  -wp WSGI_PATH, --wsgi-path WSGI_PATH  
                        Path to the WSGI module  
  -sp STATIC_PATH, --static-path STATIC_PATH  
                        Path to the static directory of the project (should be inside it), default '</PROJECT/PATH>/static'  
  -mp MEDIA_PATH, --media-path MEDIA_PATH  
                        Path to the media directory of the project (should be inside it), default '</PROJECT/PATH>/media'  
  -rp REQUIREMENTS_PATH, --requirements-path REQUIREMENTS_PATH  
                        Path to the requirements file of wsgi app  
  -pyv PYTHON_VERSION, --python-version PYTHON_VERSION  
                        Python version of WSGI application (only numbers), default '3.6'  
  -sn SERVER_NAME, --server-name SERVER_NAME  
                        Server name (in Nginx conf), defaut 'localhost'  
  -an APP_NAME, --app-name APP_NAME  
                        WSGI application name, default 'wsgi_app'  
  -nw NUM_WORKERS, --num-workers NUM_WORKERS  
                        The number of workers for Gunicorn, default 3  
  -bp BUILDDIR_PATH, --builddir-path BUILDDIR_PATH  
                        Path to the directory docker-compose to be run, default 'wsgi_app_composedir'  
If you decide to stop the server type:
```
docker-compose -f BUILDDIR_PATH/docker-compose.yml stop
```

To resume the server type:
```
docker-compose -f BUILDDIR_PATH/docker-compose.yml start
```

## Tips for environment configuration
### Docker

### Postgres

### Django
