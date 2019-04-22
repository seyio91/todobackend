#!/bin/bash
. /appenv/bin/activate

pip3 install -r requirements_test.txt

exec $@
