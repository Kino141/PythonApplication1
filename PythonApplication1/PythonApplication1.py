from PIL import Image
import PIL.ImageOps    

image = Image.open(r'C:\Users\ybarnaby\Documents\logo1.png')
print(image)

#inverted_image = PIL.ImageOps.invert(image)

#inverted_image.save(r'C:\Users\ybarnaby\Documents\logo2.png')