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
$ git clone https://github.com/loven-doo/wsgi_app_docker.git
```
Or you can download archive of the code via github web interface

### Install required python packages
```
$ pip3 install -r wsgi_app_docker/requirements.txt --upgrade
```

### Run the program
```
$ python3 wsgi_app_docker -pp ... -wp ... [options]
```
usage:  
&nbsp;&nbsp; wsgi_app_docker [-h] -pp PROJECT_PATH -wp WSGI_PATH [-sp STATIC_PATH] [-mp MEDIA_PATH]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [-rp REQUIREMENTS_PATH] [-pyv PYTHON_VERSION] [-sn SERVER_NAME] [-an APP_NAME]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [-nw NUM_WORKERS] [-bp BUILDDIR_PATH]  

optional arguments:  
&nbsp;&nbsp; -h, --help  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; show this help message and exit  
&nbsp;&nbsp; -pp PROJECT_PATH, --project-path PROJECT_PATH  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path to the wsgi app project directory  
&nbsp;&nbsp; -wp WSGI_PATH, --wsgi-path WSGI_PATH  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path to the WSGI module  
&nbsp;&nbsp; -sp STATIC_PATH, --static-path STATIC_PATH  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path to the static directory of the project (should be inside it), default '</PROJECT/PATH>/static'  
&nbsp;&nbsp; -mp MEDIA_PATH, --media-path MEDIA_PATH  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path to the media directory of the project (should be inside it), default '</PROJECT/PATH>/media'  
&nbsp;&nbsp; -rp REQUIREMENTS_PATH, --requirements-path REQUIREMENTS_PATH  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path to the requirements file of wsgi app  
&nbsp;&nbsp; -pyv PYTHON_VERSION, --python-version PYTHON_VERSION  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python version of WSGI application (only numbers), default '3.6'  
&nbsp;&nbsp; -sn SERVER_NAME, --server-name SERVER_NAME  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Server name (in Nginx conf), defaut 'localhost'  
&nbsp;&nbsp; -an APP_NAME, --app-name APP_NAME  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; WSGI application name, default 'wsgi_app'  
&nbsp;&nbsp; -nw NUM_WORKERS, --num-workers NUM_WORKERS  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The number of workers for Gunicorn, default 3  
&nbsp;&nbsp; -bp BUILDDIR_PATH, --builddir-path BUILDDIR_PATH  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path to the directory docker-compose to be run, default 'wsgi_app_composedir'  
  
The example is in run_example.sh  
  
If you decide to stop the server type:
```
$ docker-compose -f BUILDDIR_PATH/docker-compose.yml stop
```

To resume the server type:
```
$ docker-compose -f BUILDDIR_PATH/docker-compose.yml start
```

## Tips for environment configuration
The tips are for systems with apt package manager (Debian based). For systems without apt use other builtin package managers. Note that required packages can have other names. If you do not have root permisions programs can be installed from rpm packages (see below).
### Docker
To install Docker type:
```
$ sudo apt-get install docker docker.io docker-compose
```

Add the user runs docker image to a docker group:
```
$ sudo groupadd docker  # create docker group if it has not done
$ sudo adduser <youruser>  # create the user if it has not been done
$ sudo usermod -aG docker <youruser>
```
Log out and log back in so that your group membership is re-evaluated  
  
To list all docker images on the machine type:
```
$ docker images -a
```
To remove an image type:
```
$ docker rmi -f <image name or id>
```
To remove all images type:
```
$ docker rmi -f $(docker images -a)
```
To clean the cache and remove not used images type:
```
$ docker system prune -a
```
### PostgreSQL
The database and the web application should be installed on different machines for the production but for the developing, the database can be installed on the machine with the web application.  
  
To install PostgreSQL type:
```
$ sudo apt-get install postgresql postgresql-contrib
```

Create the database user for the application:
```
$ sudo su - postgres
postgres@name:~$ createuser --interactive -P
Enter name of role to add: <your_app_user>
Enter password for new role: 
Enter it again: 
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n
postgres@name:~$

postgres@name:~$ createdb --owner <your_app_user> <user_default_db_name>
postgres@name:~$ logout
$
```

### Django
If Django is used for the web application run commands below to create migrations in the database:
```
$ python <PATH/TO/POJECT>/manage.py makemigrations
$ python <PATH/TO/POJECT>/manage.py migrate
```
### PRoot
If you do not have the root access and the user is not in the docker group [PRoot](https://wiki.archlinux.org/index.php/PRoot) tool can be used to run another Linux system inside host system, and root access will be available for this system. Use [--kernel-release](https://github.com/proot-me/PRoot/blob/master/doc/proot/manual.txt) option for PRoot if the kernel vesrion of host sysytem is not compatible with docker.

To install it type:
```
$ sudo apt-get install proot
```
or build it from [source](https://github.com/proot-me/PRoot) (do 'make' in src/ folder).  
  
To create filesystem for proot you can use [QEMU](https://www.qemu.org/) (see below)
  
The best way to run command in proot filesystem:
```
$ proot -r <path/to/filesystem> <comand>
```
If you have no internet connection from proot filesystem (for example, 'unable to resolve host address' error running wget) try to put 'nameserver 8.8.8.8' to the first line of /etc/resolv.conf  
If the proot filesystem is old with support expired change repositories list for it (for example, for old Ubuntu vesions that are not currently supported, replace archive.ubuntu.com with old-releases.ubuntu.com in /etc/apt/sources.list)
### QEMU
This tip is for x86_64 system building. However, it can be any system you need.  
  
To install it type:
```
$ sudo apt-get install qemu-kvm qemu virt-manager virt-viewer libvirt-bin
```
  
Create virtual filesystem:
```
$ qemu-img create <fs_name>.img <img_size>  # for example, <img_size> = 5G
```
Install Linux system .iso image into created filesystem:
```
$ qemu-system-x86_64 -hda <fs_name>.img -boot d -cdrom <path/to/image>.iso -m <memory_amount>  # for eaxample <memory_amount> = 2G
```
To run the filesystem type:
```
$ qemu-system-x86_64 -hda <fs_name>.img -m <memoty_amount> -fsdev local,id=host_ubuntu,path=qemu_shared/,security_model=none
```
.iso -> .img -> .tar.gz  

### RPM packages
Linux programs can be installed from rpm packages. Download required rpm package build for the system. Then use following bash script to unpack it:
```
# $1 - rpm package path
# $2 - installation dir path

LOC=$(pwd)
CPIO=$(basename $2).cpio
rpm2cpio $1 > $CPIO
cd $2 && cpio -idv < $LOC/$CPIO
rm $LOC/$CPIO
```
Note that a program in rpm package is build as it is located in /usr/. That is usr/ folder will be in installation folder. So the paths in configs should be fixed.
