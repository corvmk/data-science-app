# data-science-app

## Getting data
Download data using `data_download.sh`

## Setting up repository
Copy `credentials.env-template` to `credentials.env`, replace default values with desired ones.

Build the `.env` file by running `make env`.

If desired - adjust the volume mount for postgres in `docker-compose.yml` - line 19, ref https://docs.docker.com/compose/compose-file/.

## Spinning up the project

Run `docker compose up`, notebook server becomes avaliable under the port you specified in your `.env` file.

Once done with your experiments, clean up the enviroment `docker compose down --rmi -v`.
