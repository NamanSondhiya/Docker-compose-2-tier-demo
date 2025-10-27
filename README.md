# Docker Multi-Tier Application

A containerized two-tier web application built with Docker Compose, featuring a Flask backend API and a Flask frontend service.

## Description

This project demonstrates a simple multi-tier architecture using Docker containers. The backend provides an API for game data, while the frontend serves a web interface that interacts with the backend.

## Architecture

- **Backend Service**: Flask API serving game data
- **Frontend Service**: Flask web app that displays data from the backend
- **Docker Network**: Isolated bridge network for secure communication

## Prerequisites

- Docker Engine (20.10.x or higher)
- Docker Compose (2.x or higher)

## Setup

1. Clone or navigate to the `docker-multi-tier` directory.

2. Build and start the services:
   ```bash
   docker-compose up --build
   ```

## Running the Application

1. Access the application:
   - Frontend: http://localhost:7001
   - Backend API: http://localhost:7000

2. Stop the application:
   ```bash
   docker-compose down
   ```

## API Endpoints

### Backend
- `/`: Hello message
- `/api`: Returns JSON data of games

### Frontend
- `/`: Main web interface
- `/api`: Proxies requests to backend API

## Files

- `docker-compose.yml`: Orchestrates the multi-container application
- `backend/`: Contains backend service files (Flask API, Dockerfile, requirements.txt, games.txt)
- `frontend/`: Contains frontend service files (Flask app, Dockerfile, requirements.txt, templates/)
