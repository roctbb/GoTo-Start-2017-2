from PIL import Image

dog = Image.open("dog.jpg")
leaves = Image.open("leaves.png")

leaves = leaves.resize((dog.width, dog.height))

dog.paste(leaves, (0,0), leaves)

dog.show()