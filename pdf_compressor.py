import PIL
from tkinter.filedialog import *
from PIL import Image

# Ask file name
FILE_Path = askopenfilename()
img = PIL.Image.open(FILE_Path)
myHeight, myWidth = img.size

# Compress image '.jpg'
img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
# Ask file 
save_path = asksaveasfilename()

# Compress File name
img.save(save_path+"_compressed.jpg")