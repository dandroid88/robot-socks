import RPi.GPIO as GPIO
#from RPIO import PWM
import time
import atexit


LEFT_DIR_PIN = 15
LEFT_SPEED_PIN = 19
RIGHT_DIR_PIN = 21
RIGHT_SPEED_PIN = 23


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEFT_DIR_PIN, GPIO.OUT)
GPIO.setup(LEFT_SPEED_PIN, GPIO.OUT)
GPIO.setup(RIGHT_DIR_PIN, GPIO.OUT)
GPIO.setup(RIGHT_SPEED_PIN, GPIO.OUT)

# FULL SPEED
#GPIO.output(LEFT_SPEED_PIN, GPIO.HIGH)
#GPIO.output(RIGHT_SPEED_PIN, GPIO.HIGH)

#servo = PWM.Servo()

def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def full_speed():
    GPIO.output(LEFT_SPEED_PIN, GPIO.HIGH)
    GPIO.output(RIGHT_SPEED_PIN, GPIO.HIGH)


def stop():
    GPIO.output(LEFT_SPEED_PIN, GPIO.LOW)
    GPIO.output(RIGHT_SPEED_PIN, GPIO.LOW)


# FORWARD
def forward():
    print 'Forward'
    GPIO.output(LEFT_DIR_PIN, GPIO.LOW)
    GPIO.output(RIGHT_DIR_PIN, GPIO.LOW)

    full_speed()


# REVERSE
def backword():
    print 'Back'
    GPIO.output(LEFT_DIR_PIN, GPIO.HIGH)
    GPIO.output(RIGHT_DIR_PIN, GPIO.HIGH)

    full_speed()


# SPIN LEFT
def spin_left():
    print 'Spin Left'
    GPIO.output(LEFT_DIR_PIN, GPIO.HIGH)
    GPIO.output(RIGHT_DIR_PIN, GPIO.LOW)

    full_speed()


# SPIN RIGHT
def spin_right():
    print 'Spin Right'
    GPIO.output(LEFT_DIR_PIN, GPIO.LOW)
    GPIO.output(RIGHT_DIR_PIN, GPIO.HIGH)

    full_speed()

def test():
    forward()
    time.sleep(1.0)
    backward()
    time.sleep(1.0)
    spin_left()
    time.sleep(3.0)
    spin_right()
    time.sleep(3.0)
    stop()
