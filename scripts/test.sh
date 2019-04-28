#!/bin/bash
. /appenv/bin/activate

pip3 download -d /build -r requirements_test.txt --no-input
#pip3 install -r requirements_test.txt

pip3 install --no-index -f /build -r requirements_test.txt

exec $@
