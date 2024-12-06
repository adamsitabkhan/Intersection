import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from utils import generate_convex_polygon, center_polygon

points = generate_convex_polygon(n=12)
print(points)
print(np.max(points, axis=0))
print(np.min(points, axis=0))
print((np.max(points, axis=0) - np.min(points, axis=0))/2)
points = center_polygon(points)

fig, ax = plt.subplots()
polygon = patches.Polygon(points, closed=True, edgecolor='black', facecolor='cyan')
ax.add_patch(polygon)
ax.set_aspect('equal', 'box')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()