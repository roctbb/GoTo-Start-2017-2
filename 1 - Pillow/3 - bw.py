from PIL import Image
from random import randint

img = Image.open("dog.jpg")
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        a = (r+g+b) // 3
        if a > 150:
            pixels[i, j] = (220, 120, 180)
        else:
            pixels[i, j] = (0,0,0)
img.show()
img.save("filtered_dog.jpg")

