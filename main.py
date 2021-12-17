import csv
import requests as requests
from PIL import Image, ImageDraw, ImageFont

with open('correct-list.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "4c6fcb5a0046484d621ab001cbb23ad7-8ed21946-d34b16f7"),
		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
			"to": ["email", "email"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})


image = Image.open("certificate-template.jpg")

font = ImageFont.truetype("arial.ttf", 70)
drawer = ImageDraw.Draw(image)
drawer.text((1140, 900), "Соломатин Виталий!", font=font, fill='black')

image.save('new_img.jpg')
image.show()


