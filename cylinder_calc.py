'''
Surface Area
Volume
Lateral Area
Base Area
'''
import math

def diameter(radius):
    return 2 * radius


def perimeter(radius):
    return 2 * math.pi * radius


def base_area(radius):
    return math.pi * (radius * radius)


def lateral_surface(radius, height):
    return 2 * math.pi * radius * height


def surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def volume(radius, height):
    return math.pi * (radius * radius) * height

def print_cylinder(radius, height):
    print("Radius: " + str(radius))
    print("Height: " + str(height))
    print("Surface Area: " + str(surface_area(radius, height)))
    print("Volume: " + str(volume(radius, height)))
    print("Lateral Area: " + str(lateral_surface(radius, height)))
    print("Base Area: " + str(base_area(radius)))
    return ""

print(print_cylinder(4, 8))