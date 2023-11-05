FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx && \
    apt-get install -y git


COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

