''' Packages & Debugging
    (1) Python Packages & Core Packages
    (2) Package Manager & External Package
    (3) Debugging
'''

import turtle
from PIL import Image

print("===== Python Packages & Core Packages =====")
''' Python Packages/Modules: Core, File and External '''
# Core Packages > https://docs.python.org/3/library

# Core package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)
# turtle.done()

print("-----")

my_file = open("material/sample.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()

# with - Context Manager
with open("material/sample.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("Done")

print("===== Package Manager & External Package =====")
''' Package Managers: pip pipenv npm yarn composer brew '''
# External package > https://pypi.org/

with Image.open("material/parzival.jpg") as img:
    resized_img = img.resize((250, 250))
    resized_img.show()
    resized_img.save("material/sample.png")


