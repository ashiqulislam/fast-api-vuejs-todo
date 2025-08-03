FROM node:slim

WORKDIR /app

COPY frontend/package.json .

RUN npm install -g pnpm

RUN pnpm install

ENTRYPOINT [ "pnpm"]

CMD [ "pnpm", "run", "dev", "--", "--host", "0.0.0.0"]