from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def generateParticipant(first_name, surname):
    name = f"{first_name} {surname}"
    badge = Image.open("./resources/participant.png")
    draw = ImageDraw.Draw(badge)
    MyFont = ImageFont.truetype("Avenir-Book.ttf", 24)

    w, h = draw.textsize(name, font=MyFont)
    print(w, h)

    draw.text(((400-w)*0.5 , 135),name,(3,20,36),font=MyFont)
    badge.save(f'./output/participants/{first_name}-{surname}.png')

if __name__ == "__main__":
    generateParticipant('Eric', 'Jiang')