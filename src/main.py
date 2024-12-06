import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from utils import generate_convex_polygon, transform_polygon

points = generate_convex_polygon(n=6)
points = transform_polygon(points)

fig, ax = plt.subplots()
polygon = patches.Polygon(points, closed=True, edgecolor='black', facecolor='cyan')
ax.add_patch(polygon)
ax.set_aspect('equal', 'box')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()