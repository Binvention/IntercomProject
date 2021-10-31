#!/usr/bin/env python3
import alsaaudio
import socket
import struct
import sys
from gpiozero import Button

button = Button(17)

device = "default"

audioIn = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, device=device, periodsize=1,format=alsaaudio.PCM_FORMAT_S8)

audioOut = alsaaudio.PCM(device=device, periodsize=1,format=alsaaudio.PCM_FORMAT_S8)

broadcastIP = ('192.168.100.255',10000)
recieve_group = ('',10000)

cast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
i = 0


while (True):
   if (button.is_pressed):
      length, data = audioIn.read()
      #audioOut.write(data)
      # Send data to the multicast group
      print(len(data), sys.stderr)
      cast.sendto(data,broadcastIP)