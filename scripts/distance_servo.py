from gpiozero import InputDevice, OutputDevice
import RPi.GPIO as GPIO
from time import sleep, time
import requests 

trig = OutputDevice(4)
echo = InputDevice(17)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(0)
sleep(2)

def servo():
    
    
    angle = 0
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2.5
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)

    angle = 180
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2.5
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)
    """
    angle = 44
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2.5
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)


    angle = 88
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2.5
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)


    angle = 140
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2.5
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)


    angle = 220
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)
"""
    angle = 0
    print("angle: {0}". format (angle))
    duty = float (angle) / 10.0 + 2.5
    print ("duty: {0}". format (duty))
    pwm.ChangeDutyCycle(duty)

    sleep(0.5)
   

def LoggingData(elapsed): 
    print (elapsed)
    now = time()

    r = requests.post("https://arcane-badlands-45756.herokuapp.com/add_data",
                    json={'time': now,
                            'value': elapsed})

    if r.status_code == requests.codes.ok:
            data = r.json()
            print("Data OK: ", data)
    else:
            print("error fetching, status is ", r.status_code)


def get_pulse_time():
    trig.on()
    sleep(0.00001)
    trig.off()

    while echo.is_active == False:
	    pulse_start = time()

    while echo.is_active == True:
	    pulse_end = time()

    sleep(0.06)

    return pulse_end - pulse_start

def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2
    return distance

while True:
    duration = get_pulse_time()
    distance = calculate_distance(duration)
    if distance < 0.1:
        LoggingData (distance)
        servo ()
        sleep (1)
    print(distance)
