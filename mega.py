import serial
import io
import time

''' 
mb0 = serial.Serial('/dev/cu.usbmodem14134702', 115200)

mb0.write(b'test/n')
time.sleep(2.5)

mb0.close()
'''

port = "/dev/cu.usbmodem14134702"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

sio = io.TextIOWrapper(io.BufferedRWPair(s, s))
'''
while True:
    data = s.readline()
    data = data[0:8]
    print(data.decode("utf-8"))
    time.sleep(1)
'''
sio.write('A\n')
sio.flush()
time.sleep(12) # gives enough time to display all the writen text

# TODO: 
'''
- Connect to all of the 25 microbits "at once" 
- find all ports ( ls /dev/{tty,cu}.* )
- python program template i.e. make the program run until ctrl+c
'''