from PIL import Image, ImageFilter

# blur radius and diameter
radius, diameter = 10, 30

# open an image
img = Image.open("image/Untitled (2).png")

# Paste image on white background
background_size = (img.size[0] + diameter, img.size[1] + diameter)
background = Image.new('RGB', background_size, (255, 255, 255))
background.paste(img, (radius, radius))

# create new images with white and black
mask_size = (img.size[0] + diameter, img.size[1] + diameter)
mask = Image.new('L', mask_size, 255)

black_size = (img.size[0] - diameter, img.size[1] - diameter)
black = Image.new('L', black_size, 0)

# create blur mask
mask.paste(black, (diameter, diameter))

# Blur image and paste blurred edge according to mask
blur = background.filter(ImageFilter.GaussianBlur(radius / 2))
background.paste(blur, mask=mask)
background.save("image/Untitled (3).png", quality=100)

# show blurred edged image in preview
background.show()