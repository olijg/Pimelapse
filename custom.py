from libcamera import Transform
from picamera2 import Picamera2
import time
from suntime import Sun, SunTimeException
import datetime

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(transform=Transform(vflip=True))
picam2.configure(camera_config)


def take_picture(filename):
    picam2.start()
    time.sleep(0.5)
    picam2.capture_file(filename)
    picam2.stop()


# Co-ordinates for sunrise and sunset times
latitude = 53.47
longitude = -2.283



# Set up loop conditions
pictureNumber = 0

while True:

    try:
        sun = Sun(latitude, longitude)
        sunrise = sun.get_local_sunrise_time()
        sunset = sun.get_local_sunset_time()
    except:
        SunTimeException

    currentTime = time.localtime()

    if currentTime.tm_hour <= sunrise.hour & currentTime.tm_min > sunrise.minute:
        if currentTime.tm_hour >= sunset.hour & currentTime.tm_min > sunset.minute:
            time.sleep(60)
        else:
            time.sleep(60)
    else:
        take_picture(f'timelapse/Picture{pictureNumber}.jpg')
        time.sleep(1200)
        pictureNumber += 1
