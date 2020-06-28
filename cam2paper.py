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

camera = PiCamera()
camera.capture('/tmp/camera.jpg')

epd = epd4in2bc.EPD()
logging.info("init and Clear")
epd.init()

size = (epd.width, epd.height)

imageY = Image.new('1', size, 255)
imageB = Image.open("/tmp/camera.jpg")
imageB = imageB.convert('1')
imageB = imageB.resize(size)
imageB.save("/tmp/paper.png")

epd.display(epd.getbuffer(imageB), epd.getbuffer(imageY))

epd.sleep()

