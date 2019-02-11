# docker-laravel
Laravel docker-compose basic env

## ENV config

BASIC only nginx+php needs:
COMPOSE_FILE=docker/compose/web-php.yaml

To add services to the docker-compose config, you can concatenate to the COMPOSE_FILE list, like so:
COMPOSE_FILE=docker/compose/base.yaml:docker/compose/postgres/postgres.yaml

see all available additional compose configs in docker/compose folder

### Docker

- ENV=dev
- COMPOSE_API_VERSION
- COMPOSE_CONVERT_WINDOWS_PATHS
- COMPOSE_FILE=docker/compose/web-php.yaml:docker/compose/postgres/postgres.yaml
- COMPOSE_HTTP_TIMEOUT
- COMPOSE_TLS_VERSION
- COMPOSE_PROJECT_NAME
- DOCKER_CERT_PATH
- DOCKER_HOST
- DOCKER_TLS_VERIFY

### PHP-FPM

- PHP_APP_PATH
- PHP_DOTENV=.laravel.env
- PHP_IDE_DEBUG_SERVERNAME=Docker
- PHP_XDEBUG_REMOTE_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')
- PHP_XDEBUG_REMOTE_PORT=9000
- PHP_XDEBUG_IDEKEY=PHPSTORM

### Web

- PHP_APP_PATH=src/laravel-app
- ANGULAR_APP_PATH=src/angular-app

### Postgres

- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB

### Redis

- REDIS_PASSWORD