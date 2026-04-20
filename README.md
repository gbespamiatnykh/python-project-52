# TASK MANAGER
Task Manager is a web application that helps users manage tasks.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/gbespamiatnykh/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gbespamiatnykh/python-project-52/actions)

### CI and SonarQube status:
[![Build](https://github.com/gbespamiatnykh/python-project-52/actions/workflows/build.yml/badge.svg)](https://github.com/gbespamiatnykh/python-project-52/actions/workflows/build.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=gbespamiatnykh_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=gbespamiatnykh_python-project-52)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=gbespamiatnykh_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=gbespamiatnykh_python-project-52)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=gbespamiatnykh_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=gbespamiatnykh_python-project-52)
## Live Demo
https://python-project-52-3y3c.onrender.com
## Tech Stack
- Python 3.11+
- Django 6+
- uv
- PostgreSQL
- psycopg2
- Whitenoise
- django-filter
- django-bootstrap 5
- pytest
- Rollbar
- python-dotenv

## Installation
### Clone the repository:
```bash
git clone git@github.com:gbespamiatnykh/python-project-52.git
```
```bash
cd python-project-52
```
### Create virtual environment and install dependencies:
```bash
make install
```
### Create a '.env' file in the project root and set:
- SECRET_KEY=your-secret-key
- DATABASE_URL=postgres://user:password@localhost:5432/dbname
### Run the application:
```bash
make run
```
