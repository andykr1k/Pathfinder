from sys import platform

if platform != "darwin" and "win32" and "win64":
    import RPi.GPIO as GPIO

from time import sleep

# Front
d1_en1a = 33
d1_en1b = 36
d1_in1 = 35
d1_in2 = 37
d1_in3 = 38
d1_in4 = 40

# Back
d2_en1a = 12
d2_en1b = 15
d2_in1 = 16
d2_in2 = 18
d2_in3 = 11
d2_in4 = 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(d1_en1a, GPIO.OUT)
GPIO.setup(d1_en1b, GPIO.OUT)
GPIO.setup(d1_in1, GPIO.OUT)
GPIO.setup(d1_in2, GPIO.OUT)
GPIO.setup(d1_in3, GPIO.OUT)
GPIO.setup(d1_in4, GPIO.OUT)

GPIO.setup(d2_en1a, GPIO.OUT)
GPIO.setup(d2_en1b, GPIO.OUT)
GPIO.setup(d2_in1, GPIO.OUT)
GPIO.setup(d2_in2, GPIO.OUT)
GPIO.setup(d2_in3, GPIO.OUT)
GPIO.setup(d2_in4, GPIO.OUT)

# p1a = GPIO.PWM(d1_en1a, 1000)
# p1b = GPIO.PWM(d1_en1b, 1000)
# p2a = GPIO.PWM(d2_en1a, 1000)
# p2b = GPIO.PWM(d2_en1b, 1000)

# p1a.ChangeDutyCycle(25)
# p1b.ChangeDutyCycle(25)
# p2a.ChangeDutyCycle(25)
# p1b.ChangeDutyCycle(25)

GPIO.output(d1_en1a, True)
GPIO.output(d1_en1b, True)
GPIO.output(d2_en1a, True)
GPIO.output(d2_en1b, True)

def TurnOffPins():
    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(1)

def clean():
    GPIO.output(d1_en1a, False)
    GPIO.output(d1_en1b, False)
    GPIO.output(d2_en1a, False)
    GPIO.output(d2_en1b, False)
    GPIO.cleanup()

def driveForward():
    GPIO.output(d2_in2, True)
    GPIO.output(d2_in3, True)
    GPIO.output(d1_in1, True)
    GPIO.output(d1_in4, True)

def driveBackward():
    GPIO.output(d2_in1, True)
    GPIO.output(d2_in4, True)
    GPIO.output(d1_in2, True)
    GPIO.output(d1_in3, True)

def driveLeft():
    GPIO.output(d2_in1, True)
    GPIO.output(d2_in3, True)
    GPIO.output(d1_in1, True)
    GPIO.output(d1_in3, True)

def driveRight():
    GPIO.output(d2_in2, True)
    GPIO.output(d2_in4, True)
    GPIO.output(d1_in2, True)
    GPIO.output(d1_in4, True)