#!/usr/bin/python
#
# Simple script to configure a XBee S1 over a serial connection on Mac OS X
#
# Requirements :
#  * python 3.X
#  * pyserial 2.7 (easy_install -U pyserial)
#
# Plug your Arduino board in your USB port
#  - plug your Xbee S1 on a ArduinoXBee Shield, and connect the shield to your Arduino
#  - Unplug the ATMEL microcontroller from your Arduino (impossible with SMD editions)
#  - Set the ArduinoXBeeBoard jumpers to USB

# Use as xbee_conf.py /dev/tty.usbmodem1411 where /dev/tty.usbmodem1411 is the name of your serial port

import serial
import time
import sys

def sendCommand(command):
  
    print("# Command : " + command)
    command="AT"+command+"\r"
    time.sleep(0.1)
    ser.write(command.encode("utf-8"))
    time.sleep(0.1)  # give the serial port sometime to receive the data
    print(">" + ser.readline().decode("utf-8"))
    return


def enterConfigurationMode():
    
    print("Entering configuration mode ... ", end='')
    time.sleep(1.2)  
    ser.write(b'+++')
    time.sleep(1.2)  # give the serial port sometime to receive the data
    if ser.readline().decode("utf-8"):
        print("OK.")
    else:
        print("Error. Quitting.")
        print("Make sure your Arduino board is connected, has the XBee connected on it but no microcontroller, and that the Xbee/USB jumpers are set to USB.")
        exit()
    return


ser = serial.Serial()
if len(sys.argv) > 1 :
    ser.port = sys.argv[1]
else:
    ser.port = "/dev/tty.usbmodem*" # Will work if only one USB device is connected

ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS     #number of bits per bytes
ser.parity = serial.PARITY_NONE     #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE  #number of stop bits

# Possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

#ser.timeout = None      #block read
ser.timeout = 1          #non-block read
#ser.timeout = 2         #timeout block read

ser.xonxoff = False      #disable software flow control
ser.rtscts = False       #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2    #timeout for write

def run():

    print("")
    print("--------------------------")
    print("|  XBee S1 Configurator  |")
    print("--------------------------")
    print("")

    try: 

        ser.open()

    except Exception as e:

        print("# Error opening serial port: ", e)

        exit()

    if ser.isOpen():

        try:

            print("Opening connection and flushing ...")

            ser.flushInput() # flush input buffer, discarding all its contents
            ser.flushOutput()# flush output buffer, aborting current output 
                             #  and discard all that is in buffer

            enterConfigurationMode()

            while True:

                input_string = input("Enter a command for the XBee: ")
                sendCommand(input_string)
            
            ser.close()

        except Exception as e1:

            print ("# Error communicating ... : ", e1)

    else:

        print ("# Cannot open serial port.")


run()