# Docker Installation

## Install yum-utils

yum install -y yum-utils

---

## Add Docker Repository

yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

---

## Install Docker

yum install -y docker-ce docker-ce-cli containerd.io

---

## Start Docker

systemctl start docker

systemctl enable docker

---

## Verify Docker

docker --version

docker info

docker run hello-world
