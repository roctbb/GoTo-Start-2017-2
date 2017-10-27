import requests
import vk
from config import token
from random import choice

session = vk.Session(access_token=token)
vk_api = vk.API(session)
records = vk_api.wall.get(domain='kinopoisk', v=5.68)

print(records)