import RPi.GPIO as GPIO          
from time import sleep

# Front Driver
d1_en1a = 15
d1_en1b = 18
d1_in1 = 13
d1_in2 = 11
d1_in3 = 12
d1_in4 = 16

# Back Driver
d2_en1a = 37
d2_en1b = 40
d2_in1 = 35
d2_in2 = 33
d2_in3 = 36
d2_in4 = 38

temp1 = 1

testing = "front"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(d1_en1a,GPIO.OUT)
GPIO.setup(d1_en1b,GPIO.OUT)
GPIO.setup(d1_in1,GPIO.OUT)
GPIO.setup(d1_in2,GPIO.OUT)
GPIO.setup(d1_in3,GPIO.OUT)
GPIO.setup(d1_in4,GPIO.OUT)

# GPIO.setup(d2_en1a,GPIO.OUT)
# GPIO.setup(d2_in1,GPIO.OUT)
# GPIO.setup(d2_in2,GPIO.OUT)

if testing == "front":
    GPIO.output(d1_en1a, True)
    GPIO.output(d1_en1b, True)

    GPIO.output(d1_in1, True)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, True)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, True)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, True)
    sleep(2)

    GPIO.output(d1_in1, True)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, True)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, True)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, True)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)
else:
    GPIO.output(d2_en1a, True)
    GPIO.output(d2_en1b, True)

    GPIO.output(d2_in1, True)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, True)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, True)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, True)
    sleep(2)

    GPIO.output(d2_in1, True)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, True)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, True)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, True)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)

GPIO.cleanup()