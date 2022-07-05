PROJECT_LOCATION=$(shell pwd)
DIRECTORY_NAME = $(shell basename ${PROJECT_LOCATION})
COMPOSE_PROJECT_NAME=${DIRECTORY_NAME}-$(shell whoami)
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)

env:
	echo "USER_ID=${USER_ID}" > .env
	echo "GROUP_ID=${GROUP_ID}" >> .env
	echo "COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}" >> .env
	cat credentials.env >> .env