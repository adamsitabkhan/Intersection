import argparse

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from utils import generate_convex_polygon, transform_polygon

def main(args):
    points = generate_convex_polygon(args.sides)
    points = transform_polygon(points)

    fig, ax = plt.subplots()
    polygon = patches.Polygon(points, closed=True, edgecolor='black', facecolor='cyan')
    ax.add_patch(polygon)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide paramaters for intersection generation")

    parser.add_argument(
        "--sides",
        type=int,
        help="An integer input for the number of polygon sides"
    )

    args = parser.parse_args()
    
    main(args)

