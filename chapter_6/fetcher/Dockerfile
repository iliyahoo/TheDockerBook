FROM ubuntu:14.04
MAINTAINER Iliya Strakovich "iliya@strakovich.com"
ENV REFRESHED_AT 2015-03-22
RUN apt-get -yqq update
RUN apt-get -yqq install wget
VOLUME [ "/var/lib/tomcat7/webapps/" ]
WORKDIR /var/lib/tomcat7/webapps/
ENTRYPOINT [ "wget" ]
CMD [ "-?" ]

# docker run -it --name sample iliyahoo/fetcher https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war