# postgres
FROM redis:5-alpine

ENV REDIS_PASSWORD password
CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]

EXPOSE 6379