FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/

