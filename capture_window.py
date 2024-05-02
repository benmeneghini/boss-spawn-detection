import cv2
import numpy as np
from PIL import ImageGrab
from time import time
import boss_detection

def capture():

    while (True):
        start = time()

        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # cv2.imshow("Live Window", screenshot)
        
        # boss_detection.detect(screenshot)

        if cv2.waitKey(1) == ord('q'):
            break
        print("FPS: ", 1.0 / (time() - start))

    cv2.destroyAllWindows()
    print("Window capture ended.")