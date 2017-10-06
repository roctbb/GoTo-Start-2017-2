from PIL import Image

img = Image.open("dog.jpg").convert("RGBA")
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        r, g, b, a = pixels[i, j]
        r = min(r + 100, 255)
        pixels[i, j] = (r, g, b, a)

img.show()
img.save("filtered_dog.jpg")

