# This python program controls the pins 4,17 which are connected to a
# motor to control the direction of a car
# and pins 24,25 which are connected to a motor to control the steering of
# the car. Movements can be controlled by a keyboard
# 
# The possible movements of an RC car are :
# - move_forward : Moves the car forward
# - stop : Stops the car
#
# 2018-28-03 - Vasileios Toukas
# - Creation
# 2018-24-04 - Vasileios Toukas
# - Added slow move function
# 2018-26-04 - Vasileios Toukas
# - Added reverse function
# 

import RPi.GPIO as io
import sys, tty, termios, time
class CControl(object):

  def __init__(self):
    # Deactivate GPIO warings
    print "Calling initializer"
    io.setmode(io.BCM)
    io.setwarnings(False)

    # Set pinout for backward move
    self.uiBackwardPin = 27
    io.setup(self.uiBackwardPin, io.OUT)
    self.objBackwardMotor = io.PWM(self.uiBackwardPin,100)
    self.objBackwardMotor.start(0)

    # Set pinout for forward move
    self.uiForwardPin = 17
    io.setup(self.uiForwardPin, io.OUT)
    self.objForwardMotor = io.PWM(self.uiForwardPin,100)
    self.objForwardMotor.start(0)


# Function to read a character from the keyboard
# This is needed to be able to controll the motors of a car with
# a keyboard connected to a raspberry pi3
  def getch(self):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Function to stop moving the car. It will set all pinouts to false
  def stop(self):
    print "stop function called"
    self.objForwardMotor.ChangeDutyCycle(0)
    self.objBackwardMotor.ChangeDutyCycle(0)
   

# Function to move direction motor forward
  def start(self):
    print "start function called"
    self.objForwardMotor.ChangeDutyCycle(28)
    self.objBackwardMotor.ChangeDutyCycle(0)

# Function to reverse motor
  def reverse(self):
    print "reverse function called"
    self.objForwardMotor.ChangeDutyCycle(0)
    self.objBackwardMotor.ChangeDutyCycle(30)

# Function to slow down (preparing to stop)
  def slowdown(self):
    print "Slow down, prepare to stop"
    self.objForwardMotor.ChangeDutyCycle(28)
    self.objBackwardMotor.ChangeDutyCycle(0)

   

