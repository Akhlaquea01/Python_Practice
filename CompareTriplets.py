# def compareTriplets(a, b):
#     big=0
#     if a>b:
#         big=a
#     else:
#         big=b
#     for i in range(0,big):
#         a=[]
#         b=[]
#         x=0;y=0
#         if int(a[i])>int(b[i]):
#             x+=1
#         elif a[i]<b[i]:
#             y+=1
#         else:
#             pass
#         print(x,y)
def compareTriplets(a, b):
    x=0
    y=0;
    for i in range(0,len(a)):
        if a[i]>b[i]:
            x+=1
        elif a[i]<b[i]:
            y+=1
        else:
            pass
    print(x,y)
a=[1,2,3]
b=[0,2,6]
compareTriplets(a,b)




'''#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    x=y=0;
    for i in range(3):
        if a[i]>b[i]:
            x+=1
        elif a[i]<b[i]:
            y+=1
        else:
            pass
    return x,y
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''