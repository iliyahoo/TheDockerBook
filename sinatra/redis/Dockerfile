FROM ubuntu:14.04
MAINTAINER Iliya Strakovich "iliya@strakovich.com"
ENV REFRESHED_AT 2015-03-21
RUN apt-get update
RUN apt-get -y install redis-server redis-tools
EXPOSE 6379
ENTRYPOINT [ "/usr/bin/redis-server" ]
CMD []

# cd TheDockerBook/sinatra/redis/
# ll Dockerfile
# docker build -t iliyahoo/redis:v1 .
# docker run -d --name redis -h redis iliyahoo/redis:v1
# docker exec -it redis bash
