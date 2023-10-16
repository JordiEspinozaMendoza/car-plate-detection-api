import torch
from PIL import Image
import io


def get_yolov5():
    # local best.pt
    model = torch.hub.load(
        "./yolov5", "custom", path="./model/best.pt", source="local"
    )  # local repo
    model.conf = 0.5
    return model
