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

GPIO.setup(d1_en1a,GPIO.OUT)
GPIO.setup(d1_en1b,GPIO.OUT)
GPIO.setup(d1_in1,GPIO.OUT)
GPIO.setup(d1_in2,GPIO.OUT)
GPIO.setup(d1_in3,GPIO.OUT)
GPIO.setup(d1_in4,GPIO.OUT)

GPIO.setup(d2_en1a,GPIO.OUT)
GPIO.setup(d2_en1b,GPIO.OUT)
GPIO.setup(d2_in1,GPIO.OUT)
GPIO.setup(d2_in2,GPIO.OUT)
GPIO.setup(d2_in3,GPIO.OUT)
GPIO.setup(d2_in4,GPIO.OUT)

# p1a = GPIO.PWM(d1_en1a, 1000)
# p1b = GPIO.PWM(d1_en1b, 1000)
# p2a = GPIO.PWM(d2_en1a, 1000)
# p2b = GPIO.PWM(d2_en1b, 1000)

GPIO.output(d1_en1a, True)
GPIO.output(d1_en1b, True)
GPIO.output(d2_en1a, True)
GPIO.output(d2_en1b, True)

def backwardFront():
    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)
    
    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, True)
    GPIO.output(d1_in3, True)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)

def forwardFront():
    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in1, True)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, True)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)

def forwardFrontRight():
    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    sleep(2)

    GPIO.output(d1_in1, True)
    GPIO.output(d1_in2, False)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    sleep(2)

def backwardFrontRight():
    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, True)
    sleep(2)

    GPIO.output(d1_in1, False)
    GPIO.output(d1_in2, False)
    sleep(2)

def forwardFrontLeft():
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, True)
    sleep(2)

    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)

def backwardFrontLeft():
    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in3, True)
    GPIO.output(d1_in4, False)
    sleep(2)

    GPIO.output(d1_in3, False)
    GPIO.output(d1_in4, False)
    sleep(2)


def backwardBack():
    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, True)
    GPIO.output(d2_in3, True)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)


def forwardBack():
    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in1, True)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, True)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)


def forwardBackRight():
    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    sleep(2)

    GPIO.output(d2_in1, True)
    GPIO.output(d2_in2, False)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    sleep(2)


def backwardBackRight():
    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, True)
    sleep(2)

    GPIO.output(d2_in1, False)
    GPIO.output(d2_in2, False)
    sleep(2)


def forwardBackLeft():
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, True)
    sleep(2)

    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)


def backwardBackLeft():
    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in3, True)
    GPIO.output(d2_in4, False)
    sleep(2)

    GPIO.output(d2_in3, False)
    GPIO.output(d2_in4, False)
    sleep(2)

# forwardFrontLeft()
# forwardFrontRight()
# forwardFront()

# backwardFrontLeft()
# backwardFrontRight()
# backwardFront()

print("What are your instructions sir? [direction, set, wheel, speed]")
instruct = input()

while (instruct != "q"):
    if instruct == "test":
        # Back Right Forward
        # GPIO.output(d2_in1, False)
        # GPIO.output(d2_in2, True)
        # sleep(2)

        # GPIO.output(d2_in1, False)
        # GPIO.output(d2_in2, False)
        # sleep(2)

        # Back Right Backward
        # GPIO.output(d2_in1, True)
        # GPIO.output(d2_in2, False)
        # sleep(2)

        # GPIO.output(d2_in1, False)
        # GPIO.output(d2_in2, False)
        # sleep(2)

        # Back Left Backward
        # GPIO.output(d2_in3, False)
        # GPIO.output(d2_in4, True)
        # sleep(2)

        # GPIO.output(d2_in3, False)
        # GPIO.output(d2_in4, False)
        # sleep(2)

        # Back Left Forward
        GPIO.output(d2_in3, True)
        GPIO.output(d2_in4, False)
        sleep(2)
        GPIO.output(d2_in3, False)
        GPIO.output(d2_in4, False)
        sleep(2)
    if instruct[0] == "f":
        if instruct[1] == "f":
            if instruct[2] == "l":
                if instruct[3] == "s":
                    # p1b.ChangeDutyCycle(25)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
                elif instruct[3] == "m":
                    # p1b.ChangeDutyCycle(50)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
                elif instruct[3] == "f":
                    # p1b.ChangeDutyCycle(75)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
            elif instruct[2] == "r":
                if instruct[3] == "s":
                    # p1a.ChangeDutyCycle(25)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                elif instruct[3] == "m":
                    # p1a.ChangeDutyCycle(50)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                elif instruct[3] == "f":
                    # p1a.ChangeDutyCycle(75)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
            elif instruct[2] == "b":
                if instruct[3] == "s":
                    # p1a.ChangeDutyCycle(25)
                    # p1b.ChangeDutyCycle(25)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)  
                elif instruct[3] == "m":
                    # p1a.ChangeDutyCycle(50)
                    # p1b.ChangeDutyCycle(50)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False) 
                elif instruct[3] == "f":
                    # p1a.ChangeDutyCycle(75)
                    # p1b.ChangeDutyCycle(75)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False) 
        elif instruct[1] == "b":
            if instruct[2] == "l":
                if instruct[3] == "s":
                    # p1b.ChangeDutyCycle(25)
                    GPIO.output(d2_in3, True)
                    GPIO.output(d2_in4, False)
                    sleep(2)
                    GPIO.output(d2_in3, False)
                    GPIO.output(d2_in4, False)
                    sleep(2)
                elif instruct[3] == "m":
                    # p1b.ChangeDutyCycle(50)
                    GPIO.output(d2_in3, True)
                    GPIO.output(d2_in4, False)
                    sleep(2)
                    GPIO.output(d2_in3, False)
                    GPIO.output(d2_in4, False)
                    sleep(2)
                elif instruct[3] == "f":
                    # p1b.ChangeDutyCycle(75)
                    GPIO.output(d2_in3, True)
                    GPIO.output(d2_in4, False)
                    sleep(2)
                    GPIO.output(d2_in3, False)
                    GPIO.output(d2_in4, False)
                    sleep(2)
            elif instruct[2] == "r":
                if instruct[3] == "s":
                    # p1a.ChangeDutyCycle(25)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                elif instruct[3] == "m":
                    # p1a.ChangeDutyCycle(50)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                elif instruct[3] == "f":
                    # p1a.ChangeDutyCycle(75)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
            elif instruct[2] == "b":
                if instruct[3] == "s":
                    # p1a.ChangeDutyCycle(25)
                    # p1b.ChangeDutyCycle(25)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)  
                elif instruct[3] == "m":
                    # p1a.ChangeDutyCycle(50)
                    # p1b.ChangeDutyCycle(50)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False) 
                elif instruct[3] == "f":
                    # p1a.ChangeDutyCycle(75)
                    # p1b.ChangeDutyCycle(75)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, True)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, True)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False) 
    elif instruct[0] == "b":
        if instruct[1] == "f":
            if instruct[2] == "l":
                if instruct[3] == "s":
                    # p1b.ChangeDutyCycle(25)
                    GPIO.output(d1_in3, True)
                    GPIO.output(d1_in4, False)
                    sleep(2)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
                elif instruct[3] == "m":
                    # p1b.ChangeDutyCycle(50)
                    GPIO.output(d1_in3, True)
                    GPIO.output(d1_in4, False)
                    sleep(2)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
                elif instruct[3] == "f":
                    # p1b.ChangeDutyCycle(75)
                    GPIO.output(d1_in3, True)
                    GPIO.output(d1_in4, False)
                    sleep(2)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
            elif instruct[2] == "r":
                if instruct[3] == "s":
                    # p1a.ChangeDutyCycle(25)
                    GPIO.output(d1_in1, True)
                    GPIO.output(d1_in2, False)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                elif instruct[3] == "m":
                    # p1a.ChangeDutyCycle(50)
                    GPIO.output(d1_in1, True)
                    GPIO.output(d1_in2, False)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                elif instruct[3] == "f":
                    # p1a.ChangeDutyCycle(75)
                    GPIO.output(d1_in1, True)
                    GPIO.output(d1_in2, False)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
            elif instruct[2] == "b":
                if instruct[3] == "s":
                    # p1a.ChangeDutyCycle(25)
                    # p1b.ChangeDutyCycle(25)
                    GPIO.output(d1_in1, True)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, True)
                    GPIO.output(d1_in4, False)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
                elif instruct[3] == "m":
                    # p1a.ChangeDutyCycle(50)
                    # p1b.ChangeDutyCycle(50)
                    GPIO.output(d1_in1, True)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, True)
                    GPIO.output(d1_in4, False)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
                elif instruct[3] == "f":
                    # p1a.ChangeDutyCycle(75)
                    # p1b.ChangeDutyCycle(75)
                    GPIO.output(d1_in1, True)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, True)
                    GPIO.output(d1_in4, False)
                    sleep(2)
                    GPIO.output(d1_in1, False)
                    GPIO.output(d1_in2, False)
                    GPIO.output(d1_in3, False)
                    GPIO.output(d1_in4, False)
    
    print("What are your instructions sir? [direction, set, wheel, speed]")
    instruct = input()

# Work on this!
# forwardBackLeft()
# forwardBackRight()
# forwardBack()

# backwardBackLeft()
# backwardBackRight()
# backwardBack()

GPIO.output(d1_en1a, False)
GPIO.output(d1_en1b, False)
GPIO.output(d2_en1a, False)
GPIO.output(d2_en1b, False)
GPIO.cleanup()