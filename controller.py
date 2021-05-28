from motors import Motors
import RPi.GPIO as GPIO
import time

# class MotorState:
#     OFF = 0
#     FORWARD = 1
#     BACKWARD = 2

class BaseController:
    def __init__(self):
        self._interface = Motors()

        # GPIO setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    def step(self, sleep=True):
        # TODO: switch debouncing
        p1, p2 = GPIO.input(7), GPIO.input(8)
        p3, p4 = GPIO.input(10), GPIO.input(12)
        if p1 == GPIO.HIGH:
            self._interface.move_motor(0, 100)
            self._interface.move_motor(1, 100)
            self._interface.move_motor(2, -100)
            self._interface.move_motor(3, -100)
        elif p2 == GPIO.HIGH:
            self._interface.move_motor(0, -100)
            self._interface.move_motor(1, -100)
            self._interface.move_motor(2, 100)
            self._interface.move_motor(3, 100)
        elif p3 == GPIO.HIGH:
            self._interface.move_motor(0, -100)
            self._interface.move_motor(1, 100)
            self._interface.move_motor(2, -100)
            self._interface.move_motor(3, 100)
        elif p4 == GPIO.HIGH:
            self._interface.move_motor(0, 100)
            self._interface.move_motor(1, -100)
            self._interface.move_motor(2, 100)
            self._interface.move_motor(3, -100)
        else:
            self._interface.stop_motors()

        time.sleep(0.1)

controller = BaseController()
while True:
    controller.step()
