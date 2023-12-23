import numpy as np
import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, dist=float('inf')):
        self.x = x
        self.y = y
        self.dist = dist

point1 = Point(0, 0)
point2 = Point(0, 0)
closest_dist = 2147483646

def distance(p1, p2):
    global closest_dist
    global point1
    global point2
    if np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2) < closest_dist:
        closest_dist = np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
        point1 = Point(p1.x, p1.y)
        point2 = Point(p2.x, p2.y)


def brute_force(points):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance(points[i], points[j])
            dist = closest_dist
            if dist < min_dist:
                min_dist = dist
    return min_dist

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    else:
        mid = len(points) // 2
        left = points[:mid]
        right = points[mid:]
        left_dist = closest_pair(left)
        right_dist = closest_pair(right)
        dist = min(left_dist, right_dist)
        mid_line = (points[mid - 1].x + points[mid].x) / 2
        mid_points = []
        for point in points:
            if mid_line - dist <= point.x <= mid_line + dist:
                mid_points.append(point)
        mid_points.sort(key=lambda p: p.y)
        for i in range(len(mid_points)):
            for j in range(i + 1, min(i + 8, len(mid_points))):
                distance(mid_points[i], mid_points[j])
                dist = min(dist, closest_dist)
        return dist

points = []
for _ in range(10): 
    x = random.randint(0, 100) 
    y = random.randint(0, 100) 
    point = Point(x, y) 
    points.append(point)
for point in points:
    print(f"X:  {point.x}  Y: {point.y}")
    
print(f"With Distance : {closest_pair(points)}")
print(f"Closest Pair With coordinates: {point1.x, point1.y} and {point2.x, point2.y}") 
