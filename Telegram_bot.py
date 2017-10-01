import requests
import json
import time
import parse_Yandex_Pogoda


token = '#не скажу'


def SendMessage(id, message):
    req = 'https://api.telegram.org/bot%s/SendMessage?chat_id=%s&text=%s' % (token,id,message)
    r = requests.get(req)
    print(json.loads(r.text))

SendMessage(user_id, 'Доброе утро!\nСегодня будет %s градуса(ов).' % (parse_Yandex_Pogoda.integ[0]))