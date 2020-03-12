# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:01:27 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-

import os
import StringIO
from PIL import Image, ImageFont, ImageDraw
import pygame

pygame.init()

def Drawtext(lst,interval):
    height = len(lst)*25
    im = Image.new("RGB", (1700, height), (255, 255, 255))
    imd = ImageDraw.Draw(im)
    font = pygame.font.Font("DejaVuSansMono.ttf", 10)
    n = 0
            
    for text in lst:
        rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))    
        sio = StringIO.StringIO()
        pygame.image.save(rtext, sio)
        sio.seek(0)    
        line = Image.open(sio)
        im.paste(line, (10, 5+n*interval))
        if n == 0 :
            t = text.split("/")
            name = t[5]
            tag = t[7].split(".")[1]
            if tag == "AllDriver":
                pstart = 125
                pend = 1500
                tagname = "driver"
            else:
                pstart = 160
                pend = 1500
                tagname = "sv"
            imd.rectangle([(160,5+n*interval),(530,5+n*interval+12)],outline="red")
        else:
            state = text[-1]
            if state == "%":
                imd.rectangle([(pstart,5+n*interval),(pend,5+n*interval+12)],outline="red")                    
        sio.close()
        n+=1

    im.save("%s_%s.png"%(name,tagname))
    
with open('a.txt','r') as f:
    tmp = []
    for i in f:
        if len(i) > 2:
            tmp.append(i.strip())
        elif len(tmp) > 0:
            Drawtext(tmp,20)
            tmp = []
    if len(tmp) > 0:
        Drawtext(tmp,20)
            
        
    
