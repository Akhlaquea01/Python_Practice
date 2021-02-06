#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input())
print(factorial(n))
