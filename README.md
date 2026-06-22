# Multi-Container Monitoring Application

## Overview

This project demonstrates how to build and manage a multi-container application using Docker and Docker Compose.

The application consists of:

* **Nginx Frontend** – Serves a simple web interface
* **Flask Backend** – Provides API responses
* **MySQL Database** – Stores application data
* **Docker Compose** – Orchestrates all services
* **Docker Volumes** – Provides persistent storage
* **Docker Networks** – Enables container-to-container communication

The primary goal of this project is to understand containerization, networking, persistent storage, and service orchestration in a real-world Docker environment.

---

## Architecture

```
Browser
   |
   v
Frontend (Nginx)
   |
   v
Backend (Flask)
   |
   v
MySQL Database
   |
   v
Docker Volume
```

---

## Technologies Used

* Docker
* Docker Compose
* Python
* Flask
* MySQL
* Nginx
* Linux

---

## Project Structure

```
multi-container-monitoring-app/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── screenshots/
│
├── docker-compose.yml
└── README.md
```

---

## Features

* Multi-container architecture
* Frontend to Backend API communication
* Backend to Database communication
* Container-to-container networking
* Persistent MySQL storage using Docker Volumes
* Service orchestration using Docker Compose
* Custom Docker Network
* CORS configuration for frontend-backend communication

---

## Docker Concepts Demonstrated

### Docker Images

Built custom images for:

* Flask Backend
* Nginx Frontend

### Docker Containers

Created and managed containers using:

```
docker run
docker ps
docker logs
docker stop
docker start
```

### Docker Networks

Used Docker Compose to automatically create a custom bridge network that allows services to communicate using container names.

Example:

```
backend → mysql
```

instead of using IP addresses.

### Docker Volumes

Implemented persistent storage for MySQL:


volumes:
  - mysql-data:/var/lib/mysql


This ensures database data survives container removal and recreation.

### Docker Compose

Managed the complete application stack using a single command:


docker-compose up -d


---

## Key Learning Outcomes

During this project I learned:

* Difference between Docker Images and Containers
* Building custom Docker Images using Dockerfiles
* Managing container lifecycle
* Docker Networking fundamentals
* Docker Volume persistence
* Service orchestration using Docker Compose
* Frontend-to-Backend communication
* Backend-to-Database communication
* Troubleshooting Docker issues
* Resolving CORS errors in web applications

---

## How to Run

### Clone Repository


git clone <repository-url>


### Move into Project Directory


cd multi-container-monitoring-app


### Start Application


docker-compose up -d --build


### Verify Running Containers


docker ps


---

## Access the Application

### Frontend


http://localhost:8080


### Backend API


http://localhost:5000


---

## Useful Docker Commands

### View Running Containers


docker ps


### View All Containers


docker ps -a


### View Logs


docker logs backend



docker logs mysql


### Inspect Network


docker network inspect multi-container-monitoring-app_default


### Inspect Volume


docker volume inspect multi-container-monitoring-app_mysql-data


### Stop Services


docker-compose down


### Rebuild Services


docker-compose up -d --build


---

## Screenshots

### Running Containers

screenshots/docker-ps.png


### Docker Network

Add screenshot here:


screenshots/docker-network.png


### Backend API Response

Add screenshot here:


screenshots/backen-api.png


---

## Resume Highlights

This project demonstrates:

* Docker Containerization
* Docker Compose Orchestration
* Docker Networking
* Docker Volumes
* Service Discovery
* Flask API Development
* Nginx Web Serving
* MySQL Integration
* Linux Command-Line Operations
* Troubleshooting and Debugging

---

## Future Improvements

* Add Prometheus Monitoring
* Add Grafana Dashboards
* Add Health Checks
* Add CI/CD using GitHub Actions
* Deploy on AWS EC2
* Add Reverse Proxy Configuration
* Add Security Scanning

---

## Author

Jeevan

Cloud Computing | DevOps | Linux | Docker | CI/CD | DevSecOps Aspirant
