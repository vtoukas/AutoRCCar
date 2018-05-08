# This program calls CStream class to create 2 sockets with the same client in different ports
# One for sending commands and one for streaming images
# Starts training session for autonomous driving
#
# Usage : python Server.py <server-ip> <server-port>
#
# 03-04-2018 - Vasileios Toukas
# - Creation
# 24-04-2018 - Vasileios Toukas
# - Added slowDown command

import sys, termios, os
import Socket
import CControl
import socket

# Create a socket object
#objServer = Socket.CSocket(sys.argv[1], int(sys.argv[2]))
uiControlIP = sys.argv[1]
uiControlPort = int(sys.argv[2])

socket_control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_control.connect((uiControlIP, uiControlPort))

objControl = CControl.CControl()
# start driving
bDrive = True
print("Waiting for commands")

# Loop awaiting for input
while bDrive:
  strReceivedCommand = socket_control.recv(1024)
  print strReceivedCommand
  if strReceivedCommand == "start":
    objControl.start()
  elif strReceivedCommand == "stop":
    objControl.stop()
  elif strReceivedCommand == "slowdown":
    objControl.slowdown()
  elif strReceivedCommand == "exit":
    objControl.stop()
    bDrive = False
    break
  else:
    print ("Unknown Command")

print("Car disconnected")


