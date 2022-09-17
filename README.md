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
