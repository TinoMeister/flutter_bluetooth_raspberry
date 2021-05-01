# sudo apt-get install bluetooth bluez libbluetooth-dev
# sudo python3 -m pip install pybluez

from bluetooth import *
import socket
import subprocess
import time

time.sleep(5)
cmd = 'sudo hciconfig hci0 piscan'
subprocess.check_output(cmd, shell = True )


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

while True:
   print("Waiting for connection on RFCOMM channel %d" % port)
   client_sock, client_info = server_sock.accept()

   try:
      while True:
         data = client_sock.recv(1024)
         if len(data) == 0: break
         print("received [%s]" % data)
         client_sock.send("tudo bem?\r\n")
   except IOError:
      pass

client_sock.close()
server_sock.close()

print("disconnected")
