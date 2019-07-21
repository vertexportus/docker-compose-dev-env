# php-fpm
FROM php:7.3-fpm-alpine

# APK installs
RUN apk update \
    && apk add --no-cache \
        $PHPIZE_DEPS \
        libzip libzip-dev \
        zlib zlib-dev \
        postgresql-dev \
    && rm -rf /var/cache/apk/*

# PHP extensions
RUN docker-php-ext-install \
        zip \
        pdo pdo_pgsql pdo_mysql mysqli \
    && docker-php-ext-enable \
        zip \
        pdo pdo_pgsql pdo_mysql mysqli
# PECL extensions (like xdebug is stupid)
RUN pecl install \
        xdebug-2.7.0RC1 \
    && docker-php-ext-enable \
        xdebug

# composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/bin/composer

# xdebug
RUN mkdir --parents /var/log/php7
ENV PHP_XDEBUG_REMOTE_HOST 172.18.0.1
ENV PHP_XDEBUG_REMOTE_PORT 9000
ENV PHP_XDEBUG_IDEKEY PHPSTORM
RUN echo -e "\nxdebug.remote_enable=1\nxdebug.remote_host=${PHP_XDEBUG_REMOTE_HOST}\nxdebug.remote_port=${PHP_XDEBUG_REMOTE_PORT}\nxdebug.remote_autostart=1\nxdebug.idekey=${PHP_XDEBUG_IDEKEY}\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

# env
ENV UID 1000
ENV GID 1000
RUN addgroup -S --gid $GID php-user \
    && adduser -S -D --uid $UID -G php-user php-user
USER php-user
WORKDIR /var/www
EXPOSE 9000

CMD ["php-fpm"]