FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN apt-get install python3-opencv -y

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

