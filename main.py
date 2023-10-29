from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from utils_api import labelImage, cutImage, readText

from segmentation import get_yolov5
import json
import io
from PIL import Image
import os

model = None

# if model is None:
#     raise Exception("Model not found")

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
    allow_credentials=True,
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
async def process_image(file: bytes = File(...)):
    image = Image.open(io.BytesIO(file))
    results = model(image)

    detect_res = results.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)

    results = labelImage(image, detect_res)
    car_plates = []

    for res in detect_res:
        if res["name"] == "car-plate":
            result = cutImage(image, res)
            text = readText(result["cv2"])

            car_plates.append({"image": result["image"], "text": text})

    return {"results": results, "car_plates": car_plates}
