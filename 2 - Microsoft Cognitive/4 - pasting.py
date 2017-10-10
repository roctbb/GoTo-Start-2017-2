from PIL import Image

image = Image.open('faces.jpg')
cat = Image.open('cat.png')

cat = cat.resize( (200, 200) )
image.paste(cat, (100, 200), cat)

image.show()
