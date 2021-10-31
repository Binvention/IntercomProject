#!/usr/bin/env python3
import alsaaudio
import socket
import struct
import sys
from gpiozero import Button

device = "default"

audioOut = alsaaudio.PCM(device=device,periodsize=1,format=alsaaudio.PCM_FORMAT_S8)

receive_group = ('',10000)
receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

receive.bind(receive_group)

localAddress = '192.168.100.1'

while(True):
   data, address = receive.recvfrom(65536)
   print(address[0],localAddress)
   if(address[0] != localAddress):
      audioOut.write(data)
      print(len(data),sys.stderr)
