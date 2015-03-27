FROM ubuntu:14.04
MAINTAINER Iliya Strakovich "iliya@strakovich.com"
ENV REFRESHED_AT 2015-03-27

RUN apt-get -qqy update
RUN apt-get -qqy install curl unzip
ADD https://dl.bintray.com/mitchellh/consul/0.3.1_linux_amd64.zip /tmp/consul.zip
RUN cd /usr/sbin && unzip /tmp/consul.zip && chmod +x /usr/sbin/consul && rm /tmp/consul.zip
ADD https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip /tmp/webui.zip
RUN cd /tmp/ && unzip webui.zip && mv dist/ /webui/
ADD consul.json /config/
EXPOSE 53/udp 8300 8301 8301/udp 8302 8302/udp 8400 8500
VOLUME ["/data"]
ENTRYPOINT [ "/usr/sbin/consul", "agent", "-config-dir=/config" ]
CMD []

# docker build -t iliyahoo/consul .
# docker run -p 8500:8500 -p 53:53/udp -h node1 --name node1 iliyahoo/consul -server -bootstrap
# docker pull jamtur01/consul
