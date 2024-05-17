import RPi.GPIO as GPIO
import time

global db

class AquaLight(db.Model):
    __tablename__ = 'light'
    id = db.Column(db.Integer, primary_key=True)
    lightchannel = db.Column(db.Integer, nullable=False)
    lightminute = db.Column(db.Integer, nullable=False)
    lightvalue = db.Column(db.SmallInteger, nullable=False)
    
    def Test():
        ledpin = 12				# PWM pin connected to LED
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(ledpin,GPIO.OUT)
        pi_pwm = GPIO.PWM(ledpin,4096)		#create PWM instance with frequency
        pi_pwm.start(0)				#start PWM of required Duty Cycle 
        for duty in range(0,100,1):
            print("Duty {}".format(duty))
            pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
            time.sleep(0.1)

if not AquaLight.query.count() > 0:
    lightup = AquaLight(lightchannel=1, lightminute=0, lightvalue=255)
    db.session.add(lightup)
    lightdown = AquaLight(lightchannel=1, lightminute=60*12, lightvalue=0)
    db.session.add(lightdown)
db.session.commit()          