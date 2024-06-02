template = "Youssef Walid Kabodan"
multi = 10.2
offset = 96
from PIL import Image
import numpy as np


def nametorgb(name:str) -> list[int]:
    name = name.lower()
    colors = []
    for c in name:
        colors.append(int(round((ord(c)-offset)*multi,0)))
    return colors

def topattern(colors:list[int]) -> list[list[int]]:
    pattern = []
    if len(colors) < 5:
        return [[]]
    x = 10
    while x < len(colors):
        pattern.append(tuple(colors[x-10:x]))
        x += 1
    return pattern



colors = nametorgb(template)
pattern = topattern(colors)
array = np.array(pattern)
print(array.size)
print(pattern)
im = Image.fromarray(array,mode="RGB")
new = im.resize((1000,1000),resample=Image.BOX)
new.show()