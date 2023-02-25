from picamera2 import Picamera2
import time

from libcamera import Transform

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(transform=Transform(vflip=True))
picam2.configure(camera_config)


def take_picture(fileName):
    picam2.start()
    time.sleep(2)
    picam2.capture_file(fileName)
    picam2.stop()


# take_picture()

# Set up loop conditions
pictureNumber = 0

while True:

    take_picture(f'/timelapse/Picture{pictureNumber}.jpg')
    time.sleep(300)
    pictureNumber += 1

