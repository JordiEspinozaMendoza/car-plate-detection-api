FROM tiangolo/uvicorn-gunicorn:python3.9-slim

ENV WORKERS_PER_CORE=4 
ENV MAX_WORKERS=24
ENV LOG_LEVEL="warning"
ENV TIMEOUT="200"

RUN mkdir /car-plate-detector

RUN apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

COPY requirements.txt /car-plate-detector

COPY . /car-plate-detector

WORKDIR /car-plate-detector

RUN cd yolov5

RUN pip install -r requirements.txt

RUN cd ..    

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]