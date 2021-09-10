ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#Add nginx and create the run folder for nginx.
RUN apt-get update && apt-get -y install cron python3

COPY rootfs /

RUN chmod 0644 /etc/cron.d/command_cron

#Launch nginx with debug options.
CMD [ "cron", "-f"]