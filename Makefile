PROJECT_LOCATION=$(shell pwd)
DIRECTORY_NAME = $(shell basename ${PROJECT_LOCATION})
COMPOSE_PROJECT_NAME=${DIRECTORY_NAME}-$(shell whoami)

env:
	echo "COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}" > .env
	cat credentials.env >> .env