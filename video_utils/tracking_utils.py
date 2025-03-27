# utils/tracking_utils.py

import math

def get_center(top_left, bottom_right):
    """Returns the center point (x, y) of a bounding box."""
    x1, y1 = top_left
    x2, y2 = bottom_right
    return ((x1 + x2) // 2, (y1 + y2) // 2)

def euclidean_distance(p1, p2):
    """Computes the Euclidean distance between two (x, y) points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def is_inside_region(center_y, court_height, region_center, region_half_height):
    """
    Check if a y-coordinate falls within a given vertical zone (e.g., kitchen).
    """
    real_y = (center_y / court_height)
    return abs(real_y - region_center) < region_half_height
