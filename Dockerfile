# Stage 1: Build the frontend
FROM node:lts-alpine as frontend_builder

WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build # Assumindo que seu package.json tem um script 'build'

# Stage 2: Build the backend and serve the frontend
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY .env.example ./

# Copy the built frontend assets from the builder stage
COPY --from=frontend_builder /app/frontend/build ./frontend/build

# Expose the port your backend API runs on (assuming port 8000 for FastAPI/Flask)
EXPOSE 8000

# Command to run the backend API (adjust if your main entry point is different)
CMD uvicorn backend.api.app:app --host 0.0.0.0 --port 8000 