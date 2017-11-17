import time
import vk
from config import group_token

session = vk.Session(access_token=group_token)
vk_api = vk.API(session)

last_id = 0

while True:
    messages = vk_api.messages.get(last_message_id=last_id, v=5.69)
    for message in messages['items']:
        vk_api.messages.send(user_id=message['user_id'], message='Привет!')

    if len(messages['items']) != 0:
        last_id = messages['items'][0]['id']

    time.sleep(10)