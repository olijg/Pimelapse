from picamera2 import Picamera2
import time

from libcamera import Transform

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(transform=Transform(vflip=True))
picam2.configure(camera_config)


def take_picture(filename):
    picam2.start()
    time.sleep(0.5)
    picam2.capture_file(filename)


# take_picture()

# Set up loop conditions
pictureNumber = 0

while True:

    take_picture(f'/timelapse/Picture{pictureNumber}.jpg')
    time.sleep(300)
    pictureNumber += 1

