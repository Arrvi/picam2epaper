#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from waveshare_epd import epd4in2bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from picamera import PiCamera

logging.basicConfig(level=logging.DEBUG)

epd = epd4in2bc.EPD()
size = (epd.width, epd.height)
camera = PiCamera()
camera.resolution = size
camera.capture('/tmp/camera.jpg')

logging.info("image saved")


image = Image.open("/tmp/camera.jpg")
image = image.convert('P', None, None, 1, 3)
image = image.resize(size)

imageY = Image.new('1', size, 0)
imageB = Image.new('1', size, 0)

for x in range(0, size[0]):
	for y in range(0, size[1]):
		point = (x, y)
		if image.getpixel(point) == 1:
			imageY.putpixel(point, 0)
			imageB.putpixel(point, 255)
		elif image.getpixel(point) == 2:
			imageY.putpixel(point, 255)
			imageB.putpixel(point, 0)
		else:
			imageY.putpixel(point, 255)
			imageB.putpixel(point, 255)

image.save("/tmp/paper.png")
imageY.save("/tmp/paperY.png")
imageB.save("/tmp/paperB.png")

logging.info("image converted")

epd.init()
epd.display(epd.getbuffer(imageB), epd.getbuffer(imageY))

epd.sleep()

