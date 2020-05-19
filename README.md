# Python OPC UA Method

## General

This are the source file, I have used for my video about adding methods to a OPC UA Server written in Python 3. Here is a [Link](add_me) to my video.

## Content

Here are two Python files:
- segmentdisplay.py: Contains a class to controll a 7 segment display connected to a IC and a function which sets the dot of the display
- OPC_Server.py: Contains a OPC UA server with a method to set the segment display

## Dependencies

For using the script without a raspberry pi, just uncomment the import of segmentdisplay and the two lines below the print in the function set_display.

To run the scripts make sure you have installed the OPC UA Python modul.

~~~
sudo pip install opcua
~~~

