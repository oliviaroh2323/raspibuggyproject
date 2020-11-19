import cv2
import gpiozero
import numpy as np
from time import sleep
import explorerhat


    # go backwards
explorerhat.motor.one.backward(30)
explorerhat.motor.two.forward(30)

sleep(1)

    # stop motors
explorerhat.motor.one.speed(0)
explorerhat.motor.two.speed(0)

sleep(2)

    # spin a little
explorerhat.motor.one.forward(40)
explorerhat.motor.two.forward(40)

sleep(1)

    # stop motors
explorerhat.motor.one.speed(0)
explorerhat.motor.two.speed(0)

sleep(2)

    # go backwards
explorerhat.motor.one.backward(30)
explorerhat.motor.two.forward(30)

sleep(1)

    # stop motors
explorerhat.motor.one.speed(0)
explorerhat.motor.two.speed(0)

sleep(2)

    # spin a little
explorerhat.motor.one.forward(40)
explorerhat.motor.two.forward(40)

sleep(1)

    # stop motors
explorerhat.motor.one.speed(0)
explorerhat.motor.two.speed(0)

sleep(2)

    # go backwards
explorerhat.motor.one.backward(30)
explorerhat.motor.two.forward(30)

    # stop motors
explorerhat.motor.one.speed(0)
explorerhat.motor.two.speed(0)

sleep(2)

# stop motors
explorerhat.motor.one.speed(0)
explorerhat.motor.two.speed(0)

sleep(2)

exit()