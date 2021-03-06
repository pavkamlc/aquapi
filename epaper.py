#!/usr/bin/python3
# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import traceback
import time
from lib.waveshare_epd import epd2in7
import logging
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)


# logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in7 Demo")
    epd = epd2in7.EPD()

    '''2Gray(Black and white) display'''
    logging.info("init and Clear")
    # epd.init()
    # epd.Clear(0xFF)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)

    # Drawing on the Horizontal image
    #logging.info("1.Drawing on the Horizontal image...")
    # Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    #draw = ImageDraw.Draw(Himage)
    #draw.text((10, 0), 'AkvaPI', font = font24, fill = 0)
    #draw.line((20, 50, 70, 100), fill = 0)
    #draw.line((70, 50, 20, 100), fill = 0)
    #draw.rectangle((20, 50, 70, 100), outline = 0)
    #draw.line((165, 50, 165, 100), fill = 0)
    #draw.line((140, 75, 190, 75), fill = 0)
    #draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    #draw.rectangle((80, 50, 130, 100), fill = 0)
    #draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    # epd.display(epd.getbuffer(Himage))
    # time.sleep(1)

    #logging.info("3.read bmp file")
    #Himage = Image.open(os.path.join(picdir, '2in7.bmp'))
    # epd.display(epd.getbuffer(Himage))
    # time.sleep(2)

    #logging.info("4.read bmp file on window")
    # Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    #bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    #Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2))
    # time.sleep(2)

    '''4Gray display'''
    logging.info("4Gray display--------------------------------")
    epd.Init_4Gray()
    epd.Clear(0x0)  # color to clear 0x00-0xFF
    Himage = Image.new('L', (epd.height, epd.width),
                       255)  # 255: clear the frame

    # Limage = Image.new('L', (epd.width, epd.height), 0)  # 255: clear the frame
    #draw = ImageDraw.Draw(Limage)
    #draw.text((40, 110), 'AkvaPI', font = font18, fill = epd.GRAY1)
    #draw.line((10, 140, 60, 190), fill = epd.GRAY1)
    #draw.line((60, 140, 10, 190), fill = epd.GRAY1)
    #draw.rectangle((10, 140, 60, 190), outline = epd.GRAY1)
    #draw.line((95, 140, 95, 190), fill = epd.GRAY1)
    #draw.line((70, 165, 120, 165), fill = epd.GRAY1)
    #draw.arc((70, 140, 120, 190), 0, 360, fill = epd.GRAY1)
    #draw.rectangle((10, 200, 60, 250), fill = epd.GRAY1)
    #draw.chord((70, 200, 120, 250), 0, 360, fill = epd.GRAY1)
    # epd.display_4Gray(epd.getbuffer_4Gray(Limage))
    # time.sleep(2)

    # display 4Gra bmp
    #Himage = Image.open(os.path.join(picdir, '2in7_Scale.bmp'))
    # epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    # time.sleep(2)

    #logging.info("1.Drawing on the L image...")
    # Limage = Image.new('L', (epd.width, epd.height), 0)  # 255: clear the frame
    #draw = ImageDraw.Draw(Limage)
    #draw.text((40, 110), 'AkvaPI', font = font18, fill = epd.GRAY1)
    #draw.line((10, 140, 60, 190), fill = epd.GRAY1)
    #draw.line((60, 140, 10, 190), fill = epd.GRAY1)
    #draw.rectangle((10, 140, 60, 190), outline = epd.GRAY1)
    #draw.line((95, 140, 95, 190), fill = epd.GRAY1)
    #draw.line((70, 165, 120, 165), fill = epd.GRAY1)
    #draw.arc((70, 140, 120, 190), 0, 360, fill = epd.GRAY1)
    #draw.rectangle((10, 200, 60, 250), fill = epd.GRAY1)
    #draw.chord((70, 200, 120, 250), 0, 360, fill = epd.GRAY1)
    # epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    # time.sleep(2)

    counter = 100
    draw = ImageDraw.Draw(Himage)
    while counter > 0:
        logging.info("loop: " + str(counter))
        #draw = ImageDraw.Draw(Himage)
        draw.text((counter, 110), 'AkvaPI', font=font18, fill=epd.GRAY2)
        draw.line((60, counter, counter, 190), fill=epd.GRAY3)
        logging.info("pre display")
        buffer = epd.getbuffer_4Gray(Himage)
        logging.info("mid display")
        epd.display_4Gray(buffer)
        logging.info("post display")
        counter -= 10
        # time.sleep(1)

    logging.info("Clear...")
    epd.Clear(0x0)
    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
