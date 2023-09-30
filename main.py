from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utils import getCarPlateImage


class Image(BaseModel):
    base64: str


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/process-image/")
def process_image(image: Image):
    result = getCarPlateImage(image)

    if result is None:
        raise HTTPException(status_code=404, detail="Image not processed correctly")

    return {"result": result}
