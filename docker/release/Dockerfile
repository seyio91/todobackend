FROM todobackend-dev:latest
MAINTAINER Seyi Obaweya <seyi_obaweya@yahoo.com>

# Copy Artifacts
COPY target /wheelhouse


# Install Application
RUN . /appenv/bin/activate && \
#    pip3 install --no-index -f /wheelhouse todobackend 
    pip3 install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse/*
