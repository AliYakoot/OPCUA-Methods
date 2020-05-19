#############################################################
#
# Datei: segmentdisplay.py
# Autor: Johannes
# Datum 23.11.2019
#
# Enthaelt eine Klasse zur Verwaltung einer 7 Segmentanzeige
# ueber einen BCD -> Segmentanzeige IC
#
#############################################################

#!/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_dot(dot):
    GPIO.setup(26, GPIO.OUT)
    if dot == True:
        GPIO.output(26, 1)
    else:
        GPIO.output(26, 0)
        

class segmentdisplay:
    """Klasse zur Steuerung einer 7 Segmentanzeige ueber einen IC"""
    def __init__(self, pinlist):
        """Initialisiert Pinliste"""
        self.set_pinlist(pinlist)
        self.HIGH_LOW={0:GPIO.LOW, 1:GPIO.HIGH}
    def set_pinlist(self, pinlist):
        """Zum nachtraeglichen Veraendern der Pinliste"""
        if len(pinlist) != 4:
            print "Pinliste muss 4 Elemente haben!"
            self.__pinlist=[]
        else:
            self.__pinlist=pinlist
            for i in pinlist:
                GPIO.setup(i, GPIO.OUT)
    def reset_display(self):
        """Zeigt Null an"""
        for i in self.__pinlist:
            GPIO.output(i, self.HIGH_LOW[0])
    def set_display(self, value):
        """Setzt display auf value"""
        if value > 9 or value < 0:
            print "Geht nicht! Kann nur bis 9 anzeigen"
            return -1
        tmp=0
        for i in self.__pinlist:
            GPIO.output(i, self.HIGH_LOW[(value & (1<<tmp))>>tmp])
            tmp+=1
