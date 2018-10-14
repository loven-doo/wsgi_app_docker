# Program for WSGI application Docker image creation
Creates Docker image with Nginx, Gunicorn and Postgres

## Requirements
Python >= 3.5.2  
Docker  
Docker Compose  
Python packages:  
- pyaml  
  
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

If you decide to stop the server type:
```
docker-compose -f <> stop
```

To resume the server type:
```
docker-compose -f <> start
```

## Tips for environment configuration
### Docker

### Postgres

### Django
