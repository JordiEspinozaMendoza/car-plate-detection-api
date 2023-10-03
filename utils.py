import cv2
import numpy as np
import base64
import io
from matplotlib import pyplot as plt
import imutils


def getCarPlateImageHaarcascade(image):
    try:
        results = []
        decoded_data = base64.b64decode(image.base64.split(",")[1])
        np_data = np.fromstring(decoded_data, np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

        img = cv2.resize(img, (620, 480))

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        n_plate_detector = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
        detections = n_plate_detector.detectMultiScale(
            gray, scaleFactor=1.05, minNeighbors=7
        )

        for x, y, w, h in detections:
            cropped_image = gray[y : y + h, x : x + w]
            pic_IObytes = io.BytesIO()

            plt.imsave(pic_IObytes, cropped_image, format="png")
            pic_IObytes.seek(0)
            pic_hash = base64.b64encode(pic_IObytes.read())

            results.append(pic_hash)

        return results
    except Exception as e:
        print(e)
        return None


def getCarPlateImage(image):
    try:
        results = []
        decoded_data = base64.b64decode(image.base64.split(",")[1])
        np_data = np.fromstring(decoded_data, np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

        img = cv2.resize(img, (620, 480))

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Bilateral Filter
        imageWithFilter = cv2.bilateralFilter(gray, 11, 17, 17)
        # Apply Canny Edge Detector
        edged = cv2.Canny(imageWithFilter, 30, 200)

        # Finding contours
        contours = cv2.findContours(
            edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)

            if len(approx) == 4:
                location = approx

                mask = np.zeros(gray.shape, np.uint8)

                cv2.drawContours(mask, [location], 0, 255, -1)
                cv2.bitwise_and(img, img, mask=mask)

                (x, y) = np.where(mask == 255)
                (x1, y1) = (np.min(x), np.min(y))
                (x2, y2) = (np.max(x), np.max(y))

                cropped_image = gray[x1 : x2 + 1, y1 : y2 + 1]
                pic_IObytes = io.BytesIO()

                plt.imsave(pic_IObytes, cropped_image, format="png")
                pic_IObytes.seek(0)
                pic_hash = base64.b64encode(pic_IObytes.read())

                results.append(pic_hash)

        return results
    except Exception as e:
        print(e)
        return None
