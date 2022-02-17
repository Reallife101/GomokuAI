import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dp, dy = 0.015, 0.05
#dp, dy = 0.01, 0.01
p = np.arange(0.0, 15.0, dp)
y = np.arange(0.0, 15.0, dy)
P,Y = np.meshgrid(p, y)
extent = np.min(p), np.max(p), np.min(y), np.max(y)
z11 = np.add.outer(range(15), range(15)) % 2
plt.imshow(z11, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)

def chess(p,y):
    return(1-p/2+p**5+y**6) * np.exp(-(p**2+y**2))
z22 = chess(P, Y)
plt.imshow(z22, alpha=0.2, interpolation="bilinear", extent=extent)
plt.title("Gomoku board")
plt.show()
# from cmath import rect
#
# grid = [ [1]*8 for n in range(8)]
#
# w = 70
#
# def setup():
#     size(800,600)
#
# def draw():
#     x, y = 0, 0
#     for row in grid:
#         for col in row:
#             rect(x, y, w, w)
#             x = x+w
#
