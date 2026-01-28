
# Apartment Price API (Mock Model)

A simple FastAPI server that exposes an apartment price prediction endpoint.
Currently uses a mock model that always returns a constant price.

## Project structure
- app/main.py: FastAPI entry point
- app/model.py: mock prediction function
- app/schemas.py: request/response schemas

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
## Kubernetes

Deploy to local Kubernetes (Docker Desktop):

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Access API:

http://localhost:30080/docs

