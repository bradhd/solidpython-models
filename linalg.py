from numpy.linalg import norm
from numpy import arccos, clip, dot

"""
Some linear algebra functions.
"""


def unit_vector(v):
    """
    The vector v divided by its Euclidean norm.
    """
    return v / norm(v)


def angle_between(u, v):
    """
    The angle (in radians) between vectors u and v.
    """
    _cos = dot(u, v) / (norm(u) * norm(v))
    return arccos(clip(_cos, -1, 1))


def proj(P, A, B):
    """
    The orthogonal projection of P onto the line AB.
    """
    return A + (B - A) * (dot(P - A, B - A) / dot(B - A, B - A))
