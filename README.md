# Multi-Tier Docker Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Powered-blue)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-Backend-green)](https://flask.palletsprojects.com/)

A containerized multi-tier web application built with Docker, featuring a Flask backend API and a Flask frontend service.

![Architecture Diagram](https://via.placeholder.com/800x400?text=Multi-Tier+Architecture+Diagram)

## 🚀 Features

- **Containerized Architecture**: Fully dockerized application with separate frontend and backend services
- **Microservices Design**: Clean separation of concerns between presentation and data layers
- **Docker Compose Integration**: One-command deployment of the entire application stack
- **RESTful API**: Backend service providing game data through a simple API
- **Responsive Frontend**: Web interface to display the application data

## 🏗️ Architecture

This project implements a classic two-tier architecture:

- **Frontend Service**: Handles user interface and requests to the backend
- **Backend Service**: Provides API endpoints and manages data
- **Docker Network**: Custom bridge network for secure service communication

## 🛠️ Tech Stack

- **Backend**: Python Flask API
- **Frontend**: Flask with HTML templates
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Networking**: Custom Docker bridge network

## 📋 Prerequisites

- Docker Engine (20.10.x or higher)
- Docker Compose (2.x or higher)
- Git

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multi-tier-docker.git
   cd multi-tier-docker
   ```

2. Start the application:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost:7001
   - Backend API: http://localhost:7000/api

4. Stop the application:
   ```bash
   docker-compose down
   ```

## 🔍 Service Details

### Backend Service

- **Port**: 8000 (container), 7000 (host)
- **Endpoints**:
  - `/`: Hello message
  - `/api`: Returns JSON data of games

### Frontend Service

- **Port**: 8001 (container), 7001 (host)
- **Endpoints**:
  - `/`: Main web interface
  - `/api`: Proxies requests to backend API

## 🧪 Testing

Test the API endpoints directly:

```bash
# Test backend API
curl http://localhost:7000/api

# Test frontend
curl http://localhost:7001
```

## 🔧 Configuration

The application uses environment variables for configuration:

- Backend URL in frontend service: `BACKEND_URL` (default: http://backend:8000)

## 🛡️ Security Considerations

- Services communicate over an isolated Docker network
- No sensitive data is stored in the application
- Container images use Alpine Linux for minimal attack surface

## 🔄 CI/CD Integration

This project is ready for CI/CD pipelines:

- GitHub Actions ready
- Jenkins pipeline compatible
- Automated Docker builds supported

## 📚 Further Development

Potential enhancements for the project:

- Add database layer for persistent storage
- Implement user authentication
- Add caching layer with Redis
- Create Kubernetes deployment manifests
- Implement automated testing

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Your Name - [GitHub Profile](https://github.com/yourusername)

---

*Made with ❤️ using Docker and Flask*