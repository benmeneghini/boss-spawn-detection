import cv2
import numpy as np
import pyautogui


def capture_window():

    while (True):

        screenshot = pyautogui.screenshot()

        cv2.imshow("Live Window", screenshot)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    print("Window capture ended.")