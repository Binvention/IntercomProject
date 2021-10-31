#!/usr/bin/env python3
import alsaaudio
import socket
import struct
import sys

#prepare audio device
device = "default"

audioOut = alsaaudio.PCM(device=device,periodsize=1,format=alsaaudio.PCM_FORMAT_S8)

#prepare network connection
receive_group = ('',10000)
receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

receive.bind(receive_group)

#read data from network and play it on audio hat
while(True):
   data, address = receive.recvfrom(65536)
   audioOut.write(data)
   print(len(data),sys.stderr)