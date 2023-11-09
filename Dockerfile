FROM python:3.7-alpine

RUN apt-get update && \
    apt-get install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

CMD ["./start.sh"]

