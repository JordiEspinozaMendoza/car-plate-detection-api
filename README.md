# Car plate detection API with FastAPI

This is a simple API for car plate detection using FastAPI and OpenCV.

## Installation

You can create a virtual environment and install the dependencies with the following commands:

1. Tenemos que instalar wsl ya sea por comando o buscando ubuntu en la windows Store, luego de instalar wsl, lo abrimos.
2. Usanmos el comando de python3 o python si te marca error.
3. Luego activamos el enviroment que creamos con el comando source venv/Scripts/activate ya que ya se creo la carpeta env.
4. Corremos el siguiente comando para instalar los modulos (pip install -r requirements.txt).
5. Ahora con todo instalado corremos el proyecto con uvicorn main:app --reload.
6. Si hay un error, corriendo el comando anterior, use el comando apt install libgl1-mesa-glx 
```bash

Hacerlos en wsl o en ubuntu si tienen windows
python3 -m venv venv
source /venv/Scripts/activate
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
