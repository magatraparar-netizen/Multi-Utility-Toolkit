
import math


def square(number):
    return number ** 2


def cube(number):
    return number ** 3


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")
    return length * width


if __name__ == "__main__":
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))
    print("Circle Area (radius 4):", round(circle_area(4), 2))
    print("Rectangle Area (5 x 3):", rectangle_area(5, 3))
