from PIL import Image

img = Image.open("dog.jpg")
pixels = img.load()
img.show()
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        r = min(r + 20, 255)
        g = min(g + 20, 255)
        b = min(b + 20, 255)
        pixels[i, j] = (r, g, b)

img.show()
img.save("filtered_dog.jpg")

