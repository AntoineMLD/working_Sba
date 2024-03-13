#!/bin/bash
file="compose.yml"
if [ -n "$1" ]
then
file="compose.$1.yml"
fi

echo "RUN $file"
docker compose down
docker compose --file=$file up --build --remove-orphans