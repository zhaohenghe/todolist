# ToDoList CLI Application

A Python command-line task manager with persistent JSON storage, Docker containerization, and automated CI/CD.

## Features

- Add, list, complete, and delete tasks from the command line
- Persistent storage using a JSON file
- Containerized with Docker for consistent cross-platform use
- Automated testing and deployment with GitHub Actions

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- (For development) Python 3.9+ and `pip` if running outside Docker

## Quick Start (with Docker)

1. **Clone the repository:**
```bash
git clone https://github.com/zhaohenghe/todolist.git
cd todolist
```

2. **Build the Docker image:**
```bash
docker build -t todolist .
```

3. **Run the CLI app with presistent storage:**
```bash
./run.sh python cli.py add --title "Sample Task" --description "Try the app" --due "2025-04-01"
./run.sh python cli.py list
```
4. **Other commands:**
- Mark a task as complete:
```bash
./run.sh python cli.py complete --index 0
```
- Delete a task
```bash
./run.sh python cli.py delete --index 0
```