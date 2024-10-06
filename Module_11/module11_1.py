from PIL import Image

img = Image.open('Волк.png')
img.rotate(45).show()
img.resize((150, 150)).show()
img.convert('L').show()

