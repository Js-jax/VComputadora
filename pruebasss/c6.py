import cv2
from cv2 import VideoCapture
import numpy as np

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):

    (ret, frame) = video.read()

    if not ret:
        print("Video completado")
        break

        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, binary) = cv2.threshold(
            gray_video, 127, 255, cv2.THRESH_BINARY)

        if ret == True:
            cv2.imshow("Car video", binary)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

video.release()
cv2.destroyAllWindows()
