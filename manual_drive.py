import CControl

# Create a control object
objcontrol = CControl.CControl()
# Set up the pinouts of all motors to false
objcontrol.stop()
    
while True:
  print "Waiting for command from keyboard"
  char = objcontrol.getch()
  if (char == 'k'):
    objcontrol.stop()
  elif (char == "i"):
    objcontrol.start()
  elif (char == "s"):
    objcontrol.slowdown()
  elif (char == "r"):
    objcontrol.reverse()
  elif (char == "x"):
    print("Program Ended")
    objcontrol.stop()
    break
