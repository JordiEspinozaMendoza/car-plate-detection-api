FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN apt-get install libsm6 libxext6  -y
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

