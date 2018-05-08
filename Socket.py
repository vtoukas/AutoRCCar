# This class creates a server socket for communicating with the remote car (client)
# It creates a socket and listens for connection
# It terminates the connection between the server and the client
#
# 29-03-2018 - Vasileios Toukas
# - Creation
# 03-04-2018 - Vasileios Toukas
# - Renamed to CSocket. Funtionalities is creating/terminating socket only
#

import socket
import sys, tty, termios, time

# Class CSocket opens a socket for communicating with a remote server
class CSocket(object):
  
  # \brief initializes a class
  # creates a tcp socket and waits for connections
  #
  # \param strServerIP : The server IP address
  # \param uiServerPort : The server listening port
  def __init__(self, strServerIP, uiServerPort):
    # create socket
    self.objSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.bSocketBinded = False
    try:
      self.objSocket.bind((strServerIP, uiServerPort))
      self.bSocketBinded = True
    except socket.error:
      print ("Bind failed")
      self.bSocketBinded = False
      
    # listening for connection
    if self.bSocketBinded == True:
      self.objSocket.listen(100)
      print ("Command Server is up and running, waiting for connections")
      (self.connection, self.address) = self.objSocket.accept()
      print ("Client is connected to server with IP:" + str(self.address))


  # \brief Function to termninate connection
  def terminateConnection(self):
    self.connection.close()
    self.objSocket.close()

