"""
Provides Image editing functions
"""

import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageFilter

# Default Values
content_font = ImageFont.truetype("/app/.fonts/DIN Condensed Bold.ttf",55)
aut_font = ImageFont.truetype("/app/.fonts/GillSans.ttc",30)
water_font = ImageFont.truetype("/app/.fonts/HelveticaNeue.ttc",20)




def print_text(con_text,con_font,divisor = 3,t_wd = 25):
    """
    Prints the text on image.
    @params con_text - content
    @params con_font - font style
    returns none
    """

    current_ht,pad = HT//divisor,25
    para = textwrap.wrap(con_text, width = t_wd)
    for line in para:
        text_con_wd,text_con_ht = DRAW_CON.textsize(line, font=con_font)
        DRAW_CON.text(((WD - text_con_wd)/2,current_ht),line, font=con_font)
        current_ht += text_con_ht + pad

def watermark(con_font):
    """
    Creates watermark on images.
    @param - con_font - font size
    """
    current_ht,pad = HT//1.20,25
    para = textwrap.wrap("@QuoteInspi",width = 25)
    for line in para:
        text_con_wd,text_con_ht = DRAW_CON.textsize(line,font=con_font)
        DRAW_CON.text(((WD - text_con_wd)/2,current_ht),line,font=con_font,fill=(255,255,255,75))
        current_ht += text_con_ht + pad
    BG_IMG.save("/app/test.jpg")

def image_edit(orientation,quote,author,word):
    """
    The image edit function blurs the image and calls rest functions for processing.
    @params - orientation
    @params - quote
    @params - author
    @params - word
    returns none
    """
    global BG_IMG,HT,WD,DRAW_CON


    BG_IMG = Image.open('/app/bg images/'+word+'.jpg')
    BG_IMG = BG_IMG.filter(ImageFilter.GaussianBlur(1.5))
    WD,HT = BG_IMG.size
    DRAW_CON = ImageDraw.Draw(BG_IMG)

    if orientation =="landscape":
        print_text(quote,content_font,t_wd=50)
        print_text(author,aut_font,divisor = 1.75,t_wd=50)
    else:
        print_text(quote,content_font)
        print_text(author,aut_font,divisor = 1.45)
    watermark(water_font)
