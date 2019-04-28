#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

while ! nc -z $host 3306 ; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

