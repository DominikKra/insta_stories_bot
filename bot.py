import time
import requests
import telegram
from configparser import ConfigParser

parser = ConfigParser()
_ = parser.read('api_keys.cfg')

key = parser.get('instagram', 'key')
account = parser.get('instagram', 'account')
token = parser.get('telegram', 'token')
chat_id = parser.get('telegram', 'chat_id')

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