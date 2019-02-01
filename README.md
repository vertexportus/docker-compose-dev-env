# docker-laravel
Laravel docker-compose basic env

## ENV config

BASIC only nginx+php needs:
COMPOSE_FILE=docker/compose/base.yaml

To add services to the docker-compose config, you can concatenate to the COMPOSE_FILE list, like so:
COMPOSE_FILE=docker/compose/base.yaml:docker/compose/postgres/postgres.yaml

see all available additional compose configs in docker/compose folder

### Docker

- ENV=dev
- COMPOSE_API_VERSION
- COMPOSE_CONVERT_WINDOWS_PATHS
- COMPOSE_FILE=docker/compose/base.yaml:docker/compose/postgres/postgres.yaml
- COMPOSE_HTTP_TIMEOUT
- COMPOSE_TLS_VERSION
- COMPOSE_PROJECT_NAME
- DOCKER_CERT_PATH
- DOCKER_HOST
- DOCKER_TLS_VERIFY

### Web/PHP

- WEB_WWW_PATH=src/laravel-app

### Postgres

- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB

### Redis

- REDIS_PASSWORD