#!/bin/python3
'''Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015'''

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    x=0;
    for i in range (len(ar)):
        x+=ar[i]
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
