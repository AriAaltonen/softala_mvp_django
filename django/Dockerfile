# Dockerfile for django

# Add a base image to build this image off of
FROM ubuntu:18.04

# define workdir
WORKDIR /django

# update
RUN apt-get update -y

# modules
RUN apt-get install -y python-pip3

#Copy file and install modules
COPY requirements.txt /django
RUN pip3 install --no-cache-dir -r /django/requirements.txt

# copy folder & files
COPY . /django

# Add a default port containers from this image should expose
EXPOSE 8000

# Add a default command for this image
CMD [ "python", " ./restwebful/manage.py runserver 0.0.0.0:8000" ]
