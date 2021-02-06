'''Sample Input

1 2 3 4 5
Sample Output

10 14'''
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    mini=0;
    maxe=0;
    for i in range(0,len(arr)-1):
        mini+=arr[i]
    for i in range(1,len(arr)):
        maxe+=arr[i]
    print(mini,maxe)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)