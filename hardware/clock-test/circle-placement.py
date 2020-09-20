#!/usr/bin/python3

import math
import sys

# sys.path.insert(1, '/usr/lib/kicad-nightly/lib/python3/dist-packages/')

from  pcbnew import * 

pcb = GetBoard()

for x in range(1,61):
	refdes = "D{0}".format(x)

	x_center = 150
	y_center = 100

	radius = 45

	angle = (360 / 60 * x) % 360

	x_led = x_center + math.cos(math.radians(angle)) * radius
	y_led = y_center + math.sin(math.radians(angle)) * radius

	part = pcb.FindModuleByReference(refdes)
	part.SetPosition(wxPoint(FromMM(x_led),FromMM(y_led)))
	part.SetOrientation((angle + 180) * -10)

	# print("Refdes: {0}, X: {1}, Y: {2}, rot: {3}".format(refdes, x_led, y_led, angle))

for x in range(1,16):
	refdes = "RN{0}".format(x)

	x_center = 150
	y_center = 100

	radius = 35

	angle = (360 / 15 * x) % 360 - 6

	x_led = x_center + math.cos(math.radians(angle)) * radius
	y_led = y_center + math.sin(math.radians(angle)) * radius

	part = pcb.FindModuleByReference(refdes)
	part.SetPosition(wxPoint(FromMM(x_led),FromMM(y_led)))
	part.SetOrientation((angle + 180) * -10)

	# print("Refdes: {0}, X: {1}, Y: {2}, rot: {3}".format(refdes, x_led, y_led, angle))

Refresh()
