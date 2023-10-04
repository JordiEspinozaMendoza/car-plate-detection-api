# Car plate detection API with FastAPI

This is a simple API for car plate detection using FastAPI and OpenCV.

## Installation

You can create a virtual environment and install the dependencies with the following commands:

```bash
Hacerlos en wsl o en ubuntu si tienen windows
python3 -m venv venv
source venv/Scripts/activate
source venv/bin/activate
pip install -r requirements.txt
si te aparece error en el uvicorn main:app --reload, correr el siguiente comando
apt install libgl1-mesa-glx
```

## Usage

You can run the API with the following command:

```bash
uvicorn main:app --reload 
```

Con esto el backend ya esta activo y ya podemos realizar las consultas correctas para el proyecto.

Then, you can go to http://localhost:8000/docs to see the documentation and test the API.
