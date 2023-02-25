from picamera2 import Picamera2
import time

from libcamera import Transform

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(transform=Transform(vflip=True))
picam2.configure(camera_config)


def take_picture():
    picam2.start()
    time.sleep(2)
    picam2.capture_file("test.jpg")
    picam2.stop()


take_picture()

# while True:
#
#     take_picture()
#     time.sleep(2100)
#
#     # If statement that will end the loop once finished
#     if time
