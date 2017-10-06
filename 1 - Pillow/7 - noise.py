from PIL import Image
from random import randint

img = Image.open("dog.jpg").convert("RGB")
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        a = randint(-150, 150)
        r = max(min(r + a, 255), 0)
        g = max(min(g + a, 255), 0)
        b = max(min(b + a, 255), 0)
        pixels[i, j] = (r, g, b, a)

img.show()
img.save("filtered_dog.jpg")

