from picamera2 import Picamera2

camera = Picamera2()
camera.start_and_capture_file("test.jpg")
