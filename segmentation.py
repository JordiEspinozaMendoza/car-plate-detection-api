import torch
from PIL import Image
import io


def get_yolov5():
    try:
        model = torch.hub.load(
            "./yolov5", "custom", path="./model/best.pt", source="local"
        )
        model.conf = 0.5
        return model
    except Exception as e:
        print(e)
        return None
