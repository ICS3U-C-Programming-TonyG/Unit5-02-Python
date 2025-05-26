#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-05-26

# Base height for area

def get_base():
    base = float(input("Enter the base of the triangle: "))
    return base


def get_height():
    height = float(input("Enter the height of the triangle: "))
    return height


def calculate_area(base, height):
    area = 0.5 * base * height
    return area


# Main program
base = get_base()
height = get_height()
area = calculate_area(base, height)
print(f"The area of the triangle is {area:.2f}")
