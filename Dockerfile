ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#Add nginx and create the run folder for nginx.
RUN apk --no-cache  add nginx;mkdir -p /run/nginx;

COPY rootfs /

#Launch nginx with debug options.
CMD [ "nginx"]