import cv2
import gpiozero
import numpy as np
from time import sleep
import explorerhat

# camera setup

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# while loop

while True:
    # go forwards
    explorerhat.motor.one.forward(30)
    explorerhat.motor.two.backward(30)

    sleep(2)

    # go backwards
    explorerhat.motor.one.backward(30)
    explorerhat.motor.two.forward(30)

    sleep(2)

    # spin a little
    explorerhat.motor.one.forward(80)
    explorerhat.motor.two.forward(80)

    sleep(2)

    # stop motors
    explorerhat.motor.one.speed(0)
    explorerhat.motor.two.speed(0)

    sleep(2)

    exit()

    # setup camera
    _, img = cap.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # color masks
    low_black = np.array([0, 0, 0])
    high_black = np.array([360l, 15, 15])
    black_mask = cv2.inRange(hsv_img, low_black, high_black)
    black = cv2.bitwise_and(img, img, mask=black_mask)

    if (low_black and high_black and black_mask and black):
        black == True

    # drive around
    explorerhat.motor.one.forward(25)
    explorerhat.motor.two.backward(25)

    # detect dark area

    if black == True:
        # go backwards
        explorerhat.motor.one.backward(30)
        explorerhat.motor.two.forward(30)

        sleep(2)

        # spin around
        explorerhat.motor.one.forward(60)
        explorerhat.motor.two.forward(60)

        sleep(2)

        # stop
        explorerhat.motor.one.speed(0)
        explorerhat.motor.two.speed(0)

        break