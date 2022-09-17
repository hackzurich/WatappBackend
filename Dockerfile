FROM python:3.10

WORKDIR /code

# Build requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app code
COPY ./src /code/src
CMD ["uvicorn", "src:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
