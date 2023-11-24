# sudo apt install python3-pil
# pil (python imagin library)

import PIL.Image


image=PIL.Image.open("images/import.png")

print(image.size)
print(image.format)