'''Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. 
Round the result to the nearest integer.'''
import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = (tip_percent/100)*meal_cost

    tax_percent = (tax_percent/100)*meal_cost
    totalCost = int(round(meal_cost + tip_percent + tax_percent))
    print(totalCost)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
solve(meal_cost, tip_percent, tax_percent)
