from PIL import Image
from random import randint

img = Image.open("dog.jpg")
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        a = (r+g+b) // 3
        pixels[i, j] = (a, a, a)
img.show()
img.save("filtered_dog.jpg")

