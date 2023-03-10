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


def the_sun_is_up():
    global currentTime
    currentTime = time.localtime()

    try:
        sun = Sun(latitude, longitude)
        sunrise = sun.get_local_sunrise_time()
        sunset = sun.get_local_sunset_time()
    except SunTimeException as e:
        print("Error: {0}.".format(e))

    if currentTime.tm_hour <= sunrise.hour and currentTime.tm_min > sunrise.minute:
        return False
    elif currentTime.tm_hour >= sunset.hour and currentTime.tm_min > sunset.minute:
        return False
    else:
        return True


while True:

    if the_sun_is_up():
        take_picture(
            f'timelapse/{currentTime.tm_year}-{currentTime.tm_mon}-{currentTime.tm_mday}-{currentTime.tm_hour}-{currentTime.tm_min}.jpg')
        time.sleep(1200)
    else:
        time.sleep(60)
