# Dockerfile for slackbot

# Add a base image to build this image off of
FROM ubuntu:18.04

# define workdir
WORKDIR /slack

# update
RUN apt-get update -y

# modules
RUN apt-get install -y python-pip3

#Copy file and install modules
COPY requirements.txt /slack
RUN pip3 install --no-cache-dir -r /slack/requirements.txt

# copy folder & files
COPY . /slack

# Add a default port containers from this image should expose
EXPOSE 5000

# Add a default command for this image
CMD [ "python", "./slack/slackbot.py" ]
