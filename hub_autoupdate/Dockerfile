ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#Add nginx and create the run folder for nginx.
RUN apk --no-cache add python3;mkdir /data

COPY rootfs /

RUN chmod 0644 /data/auto_update.py

WORKDIR /data

CMD [ "python3", "auto_update.py"]