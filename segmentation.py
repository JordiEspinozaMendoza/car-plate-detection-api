import torch


def get_yolov5():
    try:
        model = torch.hub.load("ultralytics/yolov5", "custom", path="./model/best.pt")
        model.conf = 0.5

        return model
    except Exception as e:
        print(e)
        return None
