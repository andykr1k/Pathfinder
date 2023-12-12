import RPi.GPIO as GPIO          
from time import sleep

def clean():
    GPIO.cleanup()

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

GPIO.output(d1_en1a, True)
GPIO.output(d1_en1b, True)
GPIO.output(d2_en1a, True)
GPIO.output(d2_en1b, True)

# Top Right
GPIO.output(d1_in1, False)
GPIO.output(d1_in2, False)
sleep(2)

# Top Right Backwards
GPIO.output(d1_in1, False)
GPIO.output(d1_in2, True)
sleep(2)

# Top Right Forwards
GPIO.output(d1_in1, True)
GPIO.output(d1_in2, False)
sleep(2)

GPIO.output(d1_in1, False)
GPIO.output(d1_in2, False)
sleep(2)

# Top Left
GPIO.output(d1_in3, False)
GPIO.output(d1_in4, False)
sleep(2)

# Top Left Backwards
GPIO.output(d1_in3, True)
GPIO.output(d1_in4, False)
sleep(2)

# Top Left Forwards
GPIO.output(d1_in3, False)
GPIO.output(d1_in4, True)
sleep(2)

GPIO.output(d1_in3, False)
GPIO.output(d1_in4, False)
sleep(2)

#Both
GPIO.output(d1_in1, False)
GPIO.output(d1_in2, False)
GPIO.output(d1_in3, False)
GPIO.output(d1_in4, False)
sleep(2)

#Both Fowards
GPIO.output(d1_in1, True)
GPIO.output(d1_in2, False)
GPIO.output(d1_in3, False)
GPIO.output(d1_in4, True)
sleep(2)

#Both Backwards
GPIO.output(d1_in1, False)
GPIO.output(d1_in2, True)
GPIO.output(d1_in3, True)
GPIO.output(d1_in4, False)
sleep(2)

#Both
GPIO.output(d1_in1, False)
GPIO.output(d1_in2, False)
GPIO.output(d1_in3, False)
GPIO.output(d1_in4, False)
sleep(2)

clean()