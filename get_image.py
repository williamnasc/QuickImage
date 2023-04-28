from PIL import ImageGrab

img = ImageGrab.grabclipboard()
# or ImageGrab.grab() to grab the whole screen!

print(img)

"""
AttributeError: 'NoneType' object has no attribute 'save'

it means there was no image on the clipboard when it tried to pull. Make sure to copy an image to the system 
clipboard with CTRL-C or some other method.
"""

img.save(r'imgs\paste.png', 'PNG')
# img.save(r'imgs\paste.jpg', 'JPEG')