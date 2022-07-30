import os
import time
import requests
import telegram
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['instagram_key'], os.environ['instagram_account'],os.environ['telegram_token'], os.environ['telegram_chat'])

key = os.environ['instagram_key']
account = os.environ['instagram_account']
token = os.environ['telegram_token']
chat_id = os.environ['telegram_chat']

counter = 0
taken_at = []

bot = telegram.Bot(token=token)    
url = 'https://instagramdimashirokovv1.p.rapidapi.com/stories/'+ account +'/optional'

headers = {
    'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com",
    'x-rapidapi-key': key
    }

while True:
    try:
        response = requests.request("GET", url, headers=headers)    
        r = response.json()    
        media_count = r['media_count']    
        for i in range(media_count):
            try:
                url_img = r['items'][i]['image_versions2']['candidates'][0]['url']
                taken = r['items'][i]['taken_at']
                if taken in taken_at:
                    continue
                else:
                    bot.sendPhoto(chat_id=chat_id, photo=url_img)
                    taken_at.append(taken)
            except:
                pass
    except:
        pass
    
    if counter < 2:
        counter += 1
        time.sleep(15000) # 5h
    else:
        counter = 0
        taken_at.clear()
        time.sleep(50400) # 14h