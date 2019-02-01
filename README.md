# docker-laravel
Laravel docker-compose basic env

## ENV config

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