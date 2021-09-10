ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#Add nginx and create the run folder for nginx.
RUN apk --no-cache add python3 py3-pip
RUN pip install requests

COPY rootfs /

WORKDIR /usr/share/python

CMD [ "python3", "auto_update.py"]