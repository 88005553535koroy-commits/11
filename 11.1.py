import os
from PIL import Image, ImageFilter
path = os.mkdir("sharpen")
u = "sharpen"
images = ["one.jpg", "two.jpg", "tree.jpg", "four.jpg", "five.jpg"]
for file in images:
    p = Image.open(file)
    sharpen_image = p.filter(ImageFilter.SHARPEN)
    sharpen_image.save(u + '/f' + file)