#!/bin/bash
clear
docker compose down
docker compose up --build --remove-orphans