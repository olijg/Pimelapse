from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

time.sleep(1)
metadata = picam2.capture_metadata()
picam2.capture_file("test.jpg")
picam2.stop()
print(metadata)


