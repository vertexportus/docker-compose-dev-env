from elixir:1.9-alpine

# env
ENV UID 1000
ENV GID 1000
RUN addgroup -S --gid $GID php-user \
    && adduser -S -D --uid $UID -G php-user php-user
USER phoenix-user
RUN mkdir /app
WORKDIR /app

EXPOSE 4000
CMD ["iex", "-S", "mix", "phx.server"]
