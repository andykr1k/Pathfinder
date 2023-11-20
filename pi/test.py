# from picamera import PiCamera
# import time
# import cv2

# camera = PiCamera()

# time.sleep(2)
# camera.resolution = (1280,720)
# camera.vflip = True
# camera.contrast = 10
# camera.framerate = 60
# print(camera.framerate)
# f_name = "/home/krik_pi/Desktop/Pathfinder/test.h264"

# print("Starting to record...")
# camera.start_recording(f_name)
# camera.wait_recording(10)
# camera.stop_recording()
# print("Done recording...")

# cam = cv2.VideoCapture('/home/krik_pi/Desktop/Pathfinder/test.h264')
# fps = cam.get(cv2.CAP_PROP_FPS)
# print(fps)

from picamera.array import PiRGBArray # Generates a 3D RGB array
from picamera import PiCamera # Provides a Python interface for the RPi Camera Module
import time # Provides time-related functions
import cv2 # OpenCV library
 
# Initialize the camera
camera = PiCamera()
 
# Set the camera resolution
camera.resolution = (960, 540)
 
# Set the number of frames per second
camera.framerate = 30
 
# Generates a 3D RGB array and stores it in rawCapture
raw_capture = PiRGBArray(camera, size=(960, 540))
 
# Wait a certain number of seconds to allow the camera time to warmup
time.sleep(0.1)
 
# Capture frames continuously from the camera
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
     
    # Grab the raw NumPy array representing the image
    image = frame.array
     
    # Display the frame using OpenCV
    cv2.imshow("Frame", image)
    print(camera.framerate)
    # Wait for keyPress for 1 millisecond
    key = cv2.waitKey(1) & 0xFF
     
    # Clear the stream in preparation for the next frame
    raw_capture.truncate(0)
     
    # If the `q` key was pressed, break from the loop
    if key == ord("q"):
        break