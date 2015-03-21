FROM ubuntu:14.04
MAINTAINER Iliya Strakovich "iliya@strakovich.com"
ENV REFRESHED_AT 2015-03-21
RUN apt-get -yqq update
RUN apt-get -yqq install ruby ruby-dev make nodejs
RUN gem install --no-rdoc --no-ri jekyll
VOLUME /data
VOLUME /var/www/html
WORKDIR /data
ENTRYPOINT [ "jekyll", "build", "--destination=/var/www/html" ]

# docker build -t iliyahoo/jekyll .
# docker run -v $PWD/james_blog:/data --name jekill -h jekill iliyahoo/jekyll
