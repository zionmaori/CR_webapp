FROM mongo:4.0.4
COPY db.json /db.json
CMD mongoimport --host mongodb --db cr-db --collection users --drop --file /db.json --jsonArray