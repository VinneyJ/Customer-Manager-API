# Customer Information Manager API

A comprehensive API for managing customer information. This API provides CRUD functionalities to handle customer data efficiently. It utilizes various technologies and tools for a seamless development and deployment experience.

## Features

- **Docker:** Containerization for easy deployment and management.
- **Redis and Celery:** Asynchronous task processing for improved performance.
- **Flower:** Monitor Celery tasks in real-time.
- **Django Rest Framework (DRF):** A powerful and flexible toolkit for building Web APIs.
- **Bash Scripts:** Convenient scripts for efficient database management and backups.
- **MailHog:** Test and visualize email communication during development.
- **Django Allauth:** Simplify authentication, registration, and account management.
- **Nginx:** High-performance web server for routing and serving API requests.
- **Redoc:** Interactive API documentation to facilitate API exploration.

## Getting Started

### Prerequisites

- Docker

### Installation

1. Build the project:

    ```bash
    make build
    ```

2. Start the project:

    ```bash
    make up
    ```

### Usage

- **API Documentation:** Access the API documentation at [localhost:8080/redoc](localhost:8080/redoc).
- **Celery Task Monitoring:** Monitor Celery tasks in real-time at [localhost:5555](localhost:5555).
- **MailHog Interface:** Test and visualize emails at [localhost:8025](localhost:8025).

## Development Commands

- **Show API Logs:**

    ```bash
    make show-logs-api
    ```

- **Run Flake8:**

    ```bash
    make flake8
    ```

- **Run Black Code Formatter Checks:**

    ```bash
    make black-check
    ```

- **Run Black Code Formatter and Display Differences:**

    ```bash
    make black-diff
    ```

- **Run Black Code Formatter:**

    ```bash
    make black
    ```

- **Run Isort Checks:**

    ```bash
    make isort-check
    ```

- **Run Isort and Display Differences:**

    ```bash
    make isort-diff
    ```

- **Run Isort:**

    ```bash
    make isort
    ```

- **Access Django Shell:**

    ```bash
    make shell
    ```

## Additional Commands

- **Stop and Remove Containers:**

    ```bash
    make down
    ```

- **Remove Containers Along with Volumes:**

    ```bash
    make down-v
    ```

- **Flush the Database:**

    ```bash
    make flush
    ```

- **Access PostgreSQL Shell for the Customers Database:**

    ```bash
    make customers-db
    ```

## Cleaning Up

To remove all Docker volumes created by the project:

```bash
make volume