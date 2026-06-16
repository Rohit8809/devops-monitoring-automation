# Docker Commands

## Check Docker Version

docker --version

---

## Display Docker Information

docker info

---

## Download and Run a Container

docker run hello-world

---

## List Running Containers

docker ps

---

## List All Containers

docker ps -a

---

## List Images

docker images

---

## Stop Container

docker stop CONTAINER_ID

---

## Start Container

docker start CONTAINER_ID

---

## Restart Container

docker restart CONTAINER_ID

---

## Remove Container

docker rm CONTAINER_ID

---

## Remove Image

docker rmi IMAGE_ID

---

## Pull Image

docker pull ubuntu

docker pull python:3.12

---

## Execute Command Inside Container

docker exec -it CONTAINER_ID bash

---

## View Logs

docker logs CONTAINER_ID

---

## Docker Compose

docker compose up -d

docker compose down

docker compose ps

---

## Prune Unused Resources

docker system prune -a
