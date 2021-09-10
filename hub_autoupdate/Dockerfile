ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#Add nginx and create the run folder for nginx.
RUN apk --no-cache add python3;mkdir /data

COPY rootfs /

CMD [ "python3", "data/auto_update.py"]