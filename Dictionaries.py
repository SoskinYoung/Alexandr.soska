import math

a = {"x": -1, "y": 3}
b = {"x": 1, "y": 3}
s = {"x": 0, "y": 0}
def distance(a, b):
    dx = a["x"] - b["x"]
    dy = a["y"] - b["y"]
    return math.sqrt(dx**2 + dy**2)
print(distance(s, b))