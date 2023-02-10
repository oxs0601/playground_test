from vpython import *

# Create the tesseract
tesseract = []
for x in (-1, 1):
    for y in (-1, 1):
        for z in (-1, 1):
            for w in (-1, 1):
                tesseract.append(vector(x, y, z, w))

# Draw the lines connecting the vertices of the tesseract
edges = [    (0, 1), (0, 2), (0, 4),    (1, 3), (1, 5),    (2, 3), (2, 6),    (3, 7),    (4, 5), (4, 6),    (5, 7),    (6, 7),]
lines = []
for edge in edges:
    lines.append(
        curve(
            color=color.white,
            radius=0.03,
            points=[tesseract[edge[0]], tesseract[edge[1]]],
        )
    )

# Rotate the tesseract
while True:
    rate(60)
    for i in range(len(tesseract)):
        x, y, z, w = tesseract[i].x, tesseract[i].y, tesseract[i].z, tesseract[i].w
        tesseract[i].x = y
        tesseract[i].y = z
        tesseract[i].z = w
        tesseract[i].w = x
    for line in lines:
        line.pos = line.pos
