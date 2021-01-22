from PIL import Image, ImageFont, ImageDraw, ImageFilter
import textwrap

#Preprocessing

bg_img = Image.open('bg images/thought.jpg')
bg_img = bg_img.filter(ImageFilter.GaussianBlur(1.5))
wd,ht = bg_img.size

# Defined Values
content_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Din Condensed Bold.ttf",55)
aut_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/GillSans.ttc",30)
water_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/HelveticaNeue.ttc",20)

draw_con = ImageDraw.Draw(bg_img)


quote = "Today is the day when you conquer all your feelings."
author = "- My mind"
#Watermark

# draw_watermark = ImageDraw.Draw(bg_img)
# text = '@QuoteInspi'

# font = ImageFont.truetype("/System/Library/Fonts/Supplemental/HelveticaNeue.ttc",20)
# textwd,textht = draw_watermark.textsize(text,font)

# x = (wd//10)*4
# y = ht - (ht//10)
# draw_watermark.text((x,y),text,font=font,fill=(255,255,255,75))


#content




# text_con_wd,text_con_ht = draw_con.textsize(con_text,con_font)
# draw_con.text((128,480),con_text,font=con_font)


#Textwrap method

# current_ht,pad = ht//3,25
# para = textwrap.wrap(con_text,width = 25)
# for line in para:
#     text_con_wd,text_con_ht = draw_con.textsize(line,font=con_font)
#     draw_con.text(((wd - text_con_wd)/2,current_ht),line,font=con_font)
#     print(text_con_wd)
#     current_ht += text_con_ht +pad




def print_text(con_text,con_font,divisor = 3,t_wd = 25):
    current_ht,pad = ht//divisor,25
    para = textwrap.wrap(con_text,width = t_wd)
    for line in para:
        text_con_wd,text_con_ht = draw_con.textsize(line,font=con_font)
        draw_con.text(((wd - text_con_wd)/2,current_ht),line,font=con_font)
        current_ht += text_con_ht +pad
    

def watermark(con_font):
    current_ht,pad = ht//1.25,25
    para = textwrap.wrap("@QuoteInspi",width = 25)
    for line in para:
        text_con_wd,text_con_ht = draw_con.textsize(line,font=con_font)
        draw_con.text(((wd - text_con_wd)/2,current_ht),line,font=con_font,fill=(255,255,255,75))
        current_ht += text_con_ht +pad
    bg_img.save("test.jpg")




def image_edit(orientation,quote,author):
    if orientation =="Landscape":
        print_text(quote,content_font,t_wd=50)
        print_text(author,aut_font,divisor = 1.75,t_wd=50)
        watermark(water_font)
    else:
        print_text(quote,content_font)
        print_text(author,aut_font,divisor = 1.75)
        watermark(water_font)


image_edit("Potrait",quote,author)



#draw_con.rectangle((128,96,512,768),fill=(255,255,255))
#Depending on the length of the quote change the position.
#If any character from 15 - 20 is space get the position and replace it with two new lines
#draw_context((128,288),con_text,font=con_font)

##Author - GillSans.ttc

# draw_author = ImageDraw.Draw(bg_img)
# aut_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/GillSans.ttc",30)
# aut_text = '-L.J Vanier'
