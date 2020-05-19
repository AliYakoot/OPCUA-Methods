#!/bin/python
# -*- coding: utf-8 -*-
#############################################################
#
# File: OPC_Server.py
# Author: Johannes
# Date 18.05.2020
#
# Set up an OPC UA Server, which offers a method to set the
# value of a 7 segment display + dot
#
#############################################################

# Import modules
from opcua import Server, ua, uamethod
from segmentdisplay import *

# Set up OPC UA Server
server = Server()
server.set_endpoint("opc.tcp://192.168.0.244:4840")

# Set up GPIOs
display = segmentdisplay([12, 21, 20, 16])

# Set up method
@uamethod
def set_display(parent, nr, dot):
    """Set Nr. and state of the dot of the 7 segment display"""
    print("set_display was called with the arguments: [" +str(nr) + ", " +str(dot) + "]")
    if nr not in range(10):
        return -1
    display.set_display(nr)
    set_dot(dot)
    return 1

# Add method to server
# Declare the input and output arguments

inarg_nr = ua.Argument()
inarg_nr.Name = "Nr."
inarg_nr.DataType = ua.NodeId(ua.ObjectIds.Int64)
inarg_nr.ValueRank = -1
inarg_nr.ArrayDemisions = []
inarg_nr.Description = ua.LocalizedText("Nr. to display")

inarg_dot = ua.Argument()
inarg_dot.Name = "Dot"
inarg_dot.DataType = ua.NodeId(ua.ObjectIds.Boolean)
inarg_dot.ValueRank = -1
inarg_dot.ArrayDemisions = []
inarg_dot.Description = ua.LocalizedText("State ot the dot")

outarg = ua.Argument()
outarg.Name = "Success"
outarg.DataType = ua.NodeId(ua.ObjectIds.Int64)
outarg.ValueRank = -1
outarg.ArrayDemisions = []
outarg.Description = ua.LocalizedText("Setting of display successfull?")

base = server.get_objects_node()
base.add_method(1, "Set 7 Segment Display", set_display, [inarg_nr, inarg_dot], [outarg])
# Start Server
try:
    print("Start OPC UA Server...")
    server.start()
    input("Server running! Press Return to shutdown server")
    server.stop()
except:
    print("Shut down Server...")
    server.stop()
    print("Server was shut down!")
