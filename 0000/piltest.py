from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
#open image
im = Image.open("test.jpg")
im2 = im.copy()
font = ImageFont.truetype("/Library/Fonts/AppleGothic.ttf",300)
width = im.size[0] - font.size
draw = ImageDraw.Draw(im2)

draw.text((width,0),unicode("4",'UTF-8'),font=font)
im2.show()


im2.close()
im.close()