import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


os.chdir(r'C:\Users\YourName\AppData\Local\Programs\Python\Python38-32\atbswp\practiceProg')
def createCard(name):
    card = Image.new('RGBA', (360, 288), 'white') # white bg
    flower = Image.open('flower.jpg') # previously downloaded flower picture
    card.paste(flower, (10, 40), flower)
    cutGuide = Image.new('RGBA', (364, 292), 'black')
    cutGuide.paste(card, (2, 2))

    drawObj = ImageDraw.Draw(cutGuide)
    fontsFolder = 'usr/share/fonts/TTF'
    customFont = ImageFont.truetype(os.path.join(fontsFolder,
                                                  'DejaVuSerif.ttf'), 72)
    drawObj.text((120, 100), name, fill='blue', font=customFont)

    cutGuide.save('{}-invite.png'.format(name))


with open('guests.txt') as f:
    guests = f.readlines()

for guest in guests:
    createCard(guest)

print('All invitations personalised and saved in the same folder. ')

