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

imageY = Image.new('1', size, 255)
imageB = Image.new('1', size, 255)

data = image.getdata()
dataY = [255] * len(data)
dataB = [255] * len(data)

for i in range(0, len(data)):
	if data[i] == 1:
		dataY[i] = 0
	elif data[i] == 2:
		dataB[i] = 0

imageY.putdata(dataY)
imageB.putdata(dataB)

image.save("/tmp/paper.png")
imageY.save("/tmp/paperY.png")
imageB.save("/tmp/paperB.png")

logging.info("image converted")

epd.init()
epd.display(epd.getbuffer(imageB), epd.getbuffer(imageY))

epd.sleep()

