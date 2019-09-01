FROM elixir:1.9-alpine

# packages
RUN apk update \
    && apk add --no-cache postgresql-client inotify-tools \
    && rm -rf /var/cache/apk/*

# env
ENV UID 1000
ENV GID 1000
RUN addgroup -S --gid $GID phoenix \
    && adduser -S -D --uid $UID -G phoenix phoenix
RUN mkdir /app && chown phoenix.phoenix /app
USER phoenix
WORKDIR /app

# phoenix
RUN mix local.hex --force && mix archive.install hex phx_new --force && mix local.rebar --force

# finalize
EXPOSE 4000
CMD ["/docker-entrypoint.sh"]
