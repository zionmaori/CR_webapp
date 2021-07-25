#!/bin/bash
echo "starting deploy"

docker-compose up -d mongodb mongo-seed &
sleep 5 &
sleep 20 &


wait 
docker exec  mongo_cr mongoexport --collection=users --sort "{firstname:1}"  --db=cr-db --out=users.json 

sleep 10 &

wait 
docker cp mongo_cr:/users.json . 
python app.py

sleep 5 &

wait
docker-compose up -d


