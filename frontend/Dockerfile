FROM node:20-alpine

WORKDIR /app

COPY package.json .
COPY tailwind.config.js .
COPY postcss.config.js .
RUN npm install

COPY public ./public
COPY src ./src

EXPOSE 3000

CMD ["npm", "run", "start"]
