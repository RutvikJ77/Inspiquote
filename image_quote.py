from PIL import Image, ImageFont, ImageDraw
import requests
import textwrap


# font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Black.ttf", 50)
# img = Image.open('test images/test1.jpg')
# draw = ImageDraw.Draw(img)
# draw.text((img.width//5,img.height//2), "Sky is the limit", (255,255,255), font=font)
# img.save('test.jpg')

# #Ranges of photo 
# #convert them accordingly 
# #640 for the images
# #characters count
# #accordingly placement

# # /System/Library/Fonts/Avenir Next.ttc
# #Din Condensed Bold
# #HelveticaNeue.ttc
# #Quotescap

# #Watermark
bg_img = Image.open('bg images/test1.jpg')
wd,ht = bg_img.size

draw_watermark = ImageDraw.Draw(bg_img)
text = '@QuoteInspi'

font = ImageFont.truetype("/System/Library/Fonts/Supplemental/HelveticaNeue.ttc",20)
textwd,textht = draw_watermark.textsize(text,font)
x = (wd//10)*4
y = ht - (ht//10)
draw_watermark.text((x,y),text,font=font,fill=(255,255,255,75))


#content
con_text = '"The sky is not the limit.Your mind is."'

draw_con = ImageDraw.Draw(bg_img)
con_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Din Condensed Bold.ttf",55)
# text_con_wd,text_con_ht = draw_con.textsize(con_text,con_font)
# draw_con.text((128,480),con_text,font=con_font)


#Textwrap method
current_ht,pad = ht//4,50
para = textwrap.wrap(con_text,width = 25)
for line in para:
    text_con_wd,text_con_ht = draw_con.textsize(line,font=con_font)
    draw_con.text(((wd - text_con_wd)/2,current_ht),line,font=con_font)
    print(text_con_wd)
    current_ht += text_con_ht +pad






#draw_con.rectangle((128,96,512,768),fill=(255,255,255))
#Depending on the length of the quote change the position.
#If any character from 15 - 20 is space get the position and replace it with two new lines
#draw_context((128,288),con_text,font=con_font)

##Author - GillSans.ttc

draw_author = ImageDraw.Draw(bg_img)
aut_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/GillSans.ttc",30)
aut_text = '-L.J Vanier'
draw_author.text((wd//2.5,640),aut_text,font=aut_font)

bg_img.save('test.jpg')

#rectangle breadth - 386
#rectangle height ratio - 1 7 1 1


# # ##Image resize test

# bg = Image.open('test.jpg')
# resize_bg = bg.resize((640,960))
# resize_bg.save('resize_test.jpg')