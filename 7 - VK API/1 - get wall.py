import requests
import vk
from config import token
from random import choice
from voice import say, recognize

session = vk.Session(access_token=token)
vk_api = vk.API(session)




records = vk_api.wall.get(domain='melfmru', v=5.68, count=100)

for i in range(10):
    try:
        random_record = choice(records['items'])
        say(random_record['text'])
    except:
        pass