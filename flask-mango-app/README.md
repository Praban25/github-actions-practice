Follow below steps :

1. Create new folder in your system and create docker-compose.yml file as below.

services:
  web:
    image: prabankini2026udaan/flask-mongo-app:latest
    ports:
      - "5000:5000"
    environment:
      - MONGO_URI=mongodb://mongo:27017/testdb
    depends_on:
      - mongo

  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:


2. run command 
docker compose up -d

3. run below command to verify
curl http://localhost:5000




