import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time



import Command as robot_move

cameraResolution = (320, 240)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = cameraResolution
camera.framerate = 32
camera.brightness = 60
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=cameraResolution)

# allow the camera to warmup
time.sleep(2)


def lineTrack():

 while True:


    camera.capture(rawCapture, use_video_port=True, format='bgr')

        # At this point the image is available as stream.array
    frame0 = rawCapture.array



    frameArea = frame0.shape[0] * frame0.shape[1]

    frame = cv2.GaussianBlur(frame0, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red0 = np.array([0, 50, 50])
    upper_red0 = np.array([10, 255, 255])
    # upper mask (170-180)
    lower_red1 = np.array([170, 50, 50])
    upper_red1 = np.array([180, 255, 255])

    low_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    maskB = cv2.inRange(hsv, lower_blue, upper_blue)
    maskY = cv2.inRange(hsv, low_yellow, up_yellow)
    mask0R = cv2.inRange(hsv, lower_red0, upper_red0)
    mask1R = cv2.inRange(hsv, lower_red1, upper_red1)
    maskR = mask0R + mask1R


    edgesY = cv2.Canny(maskY, 75, 150)
    edgesR = cv2.Canny(maskR, 75, 150)
    edgesB = cv2.Canny(maskB, 75, 150)

    linesR = cv2.HoughLinesP(edgesR, 1, np.pi / 180, 50, maxLineGap=50)

    linesY = cv2.HoughLinesP(edgesY, 1, np.pi / 180, 50, maxLineGap=50)

    linesB = cv2.HoughLinesP(edgesB, 1, np.pi / 180, 50, maxLineGap=50)



    # if lines is not None:
    #    for line in lines:
    #       x1, y1, x2, y2 = line[0]
    #      cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    if linesR  is not None:
      robot_move.command("Move Straight")
    elif linesB is not None:
      robot_move.command("Turn Right")
    elif linesY is not None:
      robot_move.command("Turn Left")

    else:
                 return 0

        # show original image
    cv2.imshow("Original", frame)


    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF is ord('q'):
        cv2.destroyAllWindows()
        print("Stop and close all windows")
        break

def main():
    lineTrack()

if __name__ == '__main__':
    main()