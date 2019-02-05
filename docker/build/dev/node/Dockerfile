# node
FROM alpine:3.8

# install node
RUN apk update && apk add --no-cache nodejs nodejs-npm

# env
ENV UID 1000
ENV GID 1000
RUN addgroup -S --gid $GID node-user \
    && adduser -S -D --uid $UID -G node-user node-user
USER node-user

WORKDIR /app

EXPOSE 4200

CMD ["/docker-entrypoint.sh"]