import cv2
import numpy as np
import base64
import io
from matplotlib import pyplot as plt
import imutils


def getCarPlateImage(image):
    try:
        decoded_data = base64.b64decode(image.base64.split(",")[1])
        np_data = np.fromstring(decoded_data, np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pic_IObytes = io.BytesIO()
        plt.imsave(pic_IObytes, gray, format="png")
        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read())

        imageWithFilter = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(imageWithFilter, 30, 200)

        pic_IObytes = io.BytesIO()
        plt.imsave(pic_IObytes, edged, format="png")
        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read())

        # Finding contours
        keypoints = cv2.findContours(
            edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        # Init location of number plate
        location = None
        # loop over contours
        for contour in contours:
            # approximate the contour
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break
            else:
                approx = cv2.approxPolyDP(contour, 15, True)
                if len(approx) == 4:
                    location = approx
                    break

        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0, 255, -1)
        new_image = cv2.bitwise_and(img, img, mask=mask)
        pic_IObytes = io.BytesIO()
        plt.imsave(pic_IObytes, new_image, format="png")
        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read())

        if location is None:
            return None

        (x, y) = np.where(mask == 255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))

        cropped_image = gray[x1 : x2 + 1, y1 : y2 + 1]
        pic_IObytes = io.BytesIO()

        plt.imsave(pic_IObytes, cropped_image, format="png")
        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read())

        return pic_hash
    except Exception as e:
        print(e)
        return None
