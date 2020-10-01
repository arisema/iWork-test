# iWork-test Django app

This an api developed with django and postgres for iWork.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Docker 
[How to install on your machine](https://docs.docker.com/install/)

#### docker-compose 
[How to install on your machine](https://docs.docker.com/compose/install)


## Installation

```bash
git clone https://github.com/arisema/iWork-test master
cd iWork-test
```

## Usage

```python
docker-compose up --build web_api_dev
```
Access endpoints at 0.0.0.0:5000
- POST /login {username, password}
- POST /sign-up {username, email, firstname, lastname, password}

Requires User Authentication
- GET /items
- GET /items/id/
- POST /items/ {name, quantity}
- PUT /items/id {name, qunatity}
- DELETE /items/id/


## Running the tests

```
docker-compose up --build web_api_test
```

## Deployment

A production container is available and can be run using:

```
docker-compose up --build -d web_api_prod
```
Access endpoints at 0.0.0.0:5500


## Built With

* [Django](https://www.djangoproject.com/) - API
* [PostgreSQL Database](https://www.postgresql.org/docs/12/index.html) - Database
* [Docker](https://www.docker.com/) - Used to containerize backend components
