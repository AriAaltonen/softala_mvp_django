# Dockerfile for node backend

# Add a base image to build this image off of
FROM ubuntu:18.04

# define workdir
WORKDIR /slack

# add `/backend/node_modules/.bin` to $PATH
#ENV PATH /backend/node_modules/.bin:$PATH

# copy files
COPY package.json /slack

# install npm modules
RUN npm install

# copy folder & files
COPY . /slack

# Add a default port containers from this image should expose
EXPOSE 9001

# Add a default command for this image
CMD ["npm", "run", "dev"]