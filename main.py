from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

badge = Image.open("badge.png")
draw = ImageDraw.Draw(badge)
font = ImageFont.truetype("Avenir-Book.ttf", 24)
draw.text((0, 0),"Sample Text",(3,20,36),font=font)
badge.save('sample-out.png')