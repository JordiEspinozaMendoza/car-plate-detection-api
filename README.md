# Car plate detection API with FastAPI

This is a simple API for car plate detection using FastAPI and OpenCV.

## Installation

You can create a virtual environment and install the dependencies with the following commands:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you are using Ubuntu, you may need to install the following packages:

```bash
apt-get install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
```

## Environment variables

Create a `.env` file with the following variables:

```bash
ORIGINS="http://localhost:3000"
ENV="development"
```

### Note

If you set the `ENV` variable to `production`, you will need to add the following variables:

```bash
ROBOFLOW_API_KEY="###########"
ROBOFLOW_PROJECT_NAME="###########"
ROBOFLOW_PROJECT_VERSION="###########"
```

You will need to ask for a Roboflow API key and create a project with the images and annotations.

If you set the `ENV` variable to `development`, you will be using the model from the `model` folder.

## Usage

You can run the API with the following command:

```bash
uvicorn main:app --reload
```

Then, you can go to http://localhost:8000/docs to see the documentation and test the API.
