import vk
from config import token

session = vk.Session(access_token=token)
vk_api = vk.API(session)

posts = []

for i in range(0, 5000, 100):
    result = vk_api.wall.get(domain='kinopoisk', count=100, offset=i, v=5.69)
    posts += result['items']
    if i % 1000 == 0:
        print(i)

posts = sorted(posts, key=lambda x: x['likes']['count'], reverse=True)

print(posts[0]['text'])
