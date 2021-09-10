ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#Add nginx and create the run folder for nginx.
RUN apk --no-cache add python3

COPY rootfs /

RUN echo "aaaaaaaaaaaaaaaaa"

RUN chmod 0644 /data/auto_update.py


CMD [ "python3", "/data/auto_update.py"]