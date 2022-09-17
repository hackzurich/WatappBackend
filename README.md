# Backend API for WatApp

In order to run this backend, we need to provide API secrets and a user database.

## Secrets

The secrets should be put in the following files (paths relative to repo root):
- Google API key: `__GCP_API_KEY`
   - Generate an API key from the Google Cloud Platform credentials page
- OIDC secret key: `__OIDC_KEY`
   - Generate a random value: `openssl rand -hex 32`

The simplest way to support user authentication is to put user data in `userdb.json`.

## Run main.py

```bash
uvicorn main:app --reload
```

## Build requirements

`requirements.txt` makes the Docker build easier, but has to be generated from `pipenv` every time that the version of a package changes:

```bash
pipenv requirements > requirements.txt
```

## Docker

```bash
docker build -t fastapi .
# Mount the AWS config/credentials
docker run -p 8080:80 fastapi
# Server available at localhost:8080
```


