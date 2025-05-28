# frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package.json .
COPY package-lock.json . # Ou yarn.lock
RUN npm install

COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]