from fastapi import FastAPI, Form, File
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from utils_api import labelImage, cutImage
from roboflow_utils import getPredictionFromRoboflow
import io
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Car plate detection API with Yolov5",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="0.0.1",
)

ORIGINS = os.environ.get("ORIGINS", "*")

origins = ORIGINS.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/notify/v1/health")
def get_health():
    return {
        "status": "UP",
    }


@app.get("/")
def read_root():
    return {"Hello": "adsadsa"}


@app.post("/api/process-image/")
def process_image(file: bytes = File(...)):
    try:
        detect_res = getPredictionFromRoboflow(file)

        file = Image.open(io.BytesIO(file))

        results = labelImage(file, detect_res)
        car_plates = []

        for res in detect_res:
            if res["name"] == "car-plate":
                result = cutImage(file, res)
                text = ""

                car_plates.append({"image": result["image"], "text": text})

        return {"results": results, "car_plates": car_plates}

    except Exception as e:
        print(e)
        return {"results": [], "car_plates": []}
