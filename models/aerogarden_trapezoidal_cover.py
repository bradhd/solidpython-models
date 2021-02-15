"""
For the Aerogarden Harvest. A simple replacement for the trapezoidal
cover that you remove to add water / plant food.
"""

from euclid3 import Point2
from solid import polygon, cylinder, linear_extrude, scad_render_to_file
from solid.utils import fillet_2d, forward


def isoceles_trapezoid(a, b, h):
    """
    Isoceles trapezoid in the upper half-plane,
    with parallel side lengths a,b and height h,
    with the b-side on the x-axis and centred at the origin.
    """
    return polygon([[-0.5 * b, 0], [0.5 * b, 0], [0.5 * a, h], [-0.5 * a, h]])


a = 65  # length of upper edge of trapezoid (in mm)
b = 106  # length of lower edge of trapezoid
h = 35  # height of trapezoid

r1 = 7.5  # arc radius for fillets on lower edge corners
r2 = 8.7  # arc radius for fillets on upper edge corners

thickness = 2  # thickness of trapezoid

T = isoceles_trapezoid(a, b, h)

A, B, C, D = [Point2(*x) for x in T.params["points"]]

# Add fillets to the corners
T = fillet_2d([[D, A, B], [A, B, C]], T, r1)
T = fillet_2d([[B, C, D], [C, D, A]], T, r2)
filleted_trapezoid = linear_extrude(height=thickness)(T)

# Construct handle as a cylinder at the center of the trapezoid
handle = forward(h / 2)(cylinder(h=10, r=2))

cover = filleted_trapezoid + handle

scad_render_to_file(cover, "aerogarden_trapezoidal_cover.scad")