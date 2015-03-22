FROM iliyahoo/redis:base
MAINTAINER Iliya Strakovich "iliya@strakovich.com"
ENV REFRESHED_AT 2015-03-22
ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-replica.log", "--slaveof redis_primary 6379" ]
