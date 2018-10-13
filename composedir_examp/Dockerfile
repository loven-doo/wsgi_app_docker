FROM python:3.6                                                                 
ENV PYTHONUNBUFFERED 1                                                          
RUN mkdir /config                                                               
ADD /configs/requirements.txt /configs/gunicorn_start /configs/                 
RUN apt-get update \                                                            
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \                        
    net-tools \                                                                 
  && apt-get clean \                                                            
  && rm -rf /var/lib/apt/lists/*                                                
RUN pip install gunicorn                                                        
RUN pip install -r /configs/requirements.txt --upgrade                          
RUN mkdir /wsgi_app                                                             
WORKDIR /wsgi_app 
