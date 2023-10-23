FROM ubuntu:latest
EXPOSE 8000
RUN apt-get update && \
    apt-get install -y python3 python3-pip
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]