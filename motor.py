import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#led = 11
M1 = 38
M2 = 40
M3 = 31
M4 = 33
PWMA = 37
PWMB = 32

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M3, GPIO.OUT)
GPIO.setup(M4, GPIO.OUT)

PWM_A = GPIO.PWM(PWMA, 100)
PWM_B = GPIO.PWM(PWMB, 100)

PWM_A.start(100)
PWM_B.start(100)

PWM_A.ChangeDutyCycle(100)
PWM_B.ChangeDutyCycle(100)

print("M1:1")
GPIO.output(M1, 1)
time.sleep(1)

try:
    while True:
        print("PWM:5")
        PWM_A.ChangeDutyCycle(10)
        PWM_B.ChangeDutyCycle(10)
        time.sleep(1)
        print("PWM:75")
        PWM_A.ChangeDutyCycle(20)
        PWM_B.ChangeDutyCycle(20)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
