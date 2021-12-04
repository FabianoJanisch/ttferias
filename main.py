import tweepy
from PIL import Image, ImageDraw, ImageFont
import time


consumer_key = #Consumer key
consumer_secret = # Consumer secret
access_token = # Access token
access_token_secret = # Acess token secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    time.sleep(25)
    hora = time.gmtime()
    if hora[3] == 16 and hora[4] == 00:
        data = time.gmtime()[7]
        remain = 348 - int(data)   

        phrase = (f"           Faltam {remain} dias para o fim do\nsemestre letivo da São Leopoldo Mandic")
        status = phrase.split()
        status = ' '.join(status)


        font = ImageFont.truetype("RobotoBlack.ttf", 400)
        font2 = ImageFont.truetype("RobotoBlack.ttf", 32)

        IMG = Image.open("template.png")
        IMGdraw = ImageDraw.Draw(IMG)
        IMGdraw.text((540, 640), str(remain), fill="white", anchor="ms", font=font)
        IMGdraw.multiline_text((540, 700), phrase, fill="white", anchor="ma", font=font2)
        IMG.save('post.png')
        api.update_status_with_media(status, 'post.png')
        print ('tweet enviado')
        time.sleep(82.800)
