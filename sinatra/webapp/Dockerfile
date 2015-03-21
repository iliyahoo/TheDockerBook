FROM ubuntu:14.04
MAINTAINER Iliya Strakovich "iliya@strakovich.com"
ENV REFRESHED_AT 2015-03-21
RUN apt-get update
RUN apt-get -y install ruby ruby-dev build-essential redis-tools
RUN gem install --no-rdoc --no-ri sinatra json redis
RUN mkdir -p /opt/webapp
EXPOSE 4567
CMD [ "/opt/webapp/bin/webapp" ]

# cd TheDockerBook/sinatra/webapp/
# ll Dockerfile
# docker build -t iliyahoo/webapp:v1 .
# docker run -d -p 80:4567 --name webapp -h webapp --link redis:db -v $PWD:/opt/webapp -h webapp iliyahoo/webapp:v1
# docker exec -it webapp bash

## test
# curl -i -H 'Accept: application/json' -d 'name=Foo&status=Bar' http://localhost/json
# curl -i http://localhost/json
