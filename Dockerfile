FROM ubuntu:24.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-django
WORKDIR /app
COPY * /app
RUN ls -ltr 
