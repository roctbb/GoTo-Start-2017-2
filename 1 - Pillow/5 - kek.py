from PIL import Image

img = Image.open("dog.jpg")

box = (0,0, img.width//2, img.height)
left = img.crop(box)
left = left.transpose(Image.FLIP_LEFT_RIGHT)

img.paste(left, (img.width//2, 0))


left.show()
img.show()
img.save("filtered_dog.jpg")
