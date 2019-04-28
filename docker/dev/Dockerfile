FROM seyio/todobackend-base:latest
MAINTAINER Seyi Obaweya <seyi_obaweya@yahoo.com>

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev python3-dev libmysqlclient-dev gcc

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip3 install pip --upgrade && \
    pip3 install wheel --upgrade && \
    pip3 install -U setuptools

# PIP environment variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache PIP_DOWNLOAD_CACHE=/cache

# OUTPUT: Build artefacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Test reports are output here
VOLUME /reports

#OUTPUT: Build Cache
VOLUME /build

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python3", "manage.py", "test", "--noinput"]

# Add application source
COPY src /application
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh && ln -s /usr/local/bin/wait-for-it.sh /application/wait-for-it.sh
WORKDIR /application
