xbee-conf
=========

A simple Python 3 script to configure a XBee S1 module over a simple serial connection using a bare Arduino board


## Requirements :

For this you will need

  - python 3.X
  - pyserial 2.7 (`easy_install -U pyserial`)
  - An Arduino board (not an SMD edition)
  - An ArduinoXBee Shield
  - An XBee S1

## Usage

  - Unplug the ATMEL microcontroller from your Arduino (impossible with SMD editions)
  - Plug your Xbee S1 on a ArduinoXBee Shield, and connect the shield to your Arduino
  - Plug your Arduino board in your USB port. 
  - Set the ArduinoXBeeBoard jumpers to USB

Then :

    python3.3 xbee_conf.py /dev/tty.usbmodem1411

where `/dev/tty.usbmodem1411` is the name of your serial port for instance


> NB : The XBee S1 will close the connection automatically after a few seconds so you will need to reconnect eventually.