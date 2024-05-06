import cv2
from ultralytics import YOLO


def detect(image_path): #start with path, later directly with image
    image = cv2.imread(image_path)

    model = YOLO(weights='best.pt')
    model.predict(image_path, save=True)