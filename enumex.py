from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

print(Color.red)
print(type(Color.red))
print(isinstance(Color.green, Color))

lightcol = Color.red
print(lightcol.name)
print(lightcol.value)



