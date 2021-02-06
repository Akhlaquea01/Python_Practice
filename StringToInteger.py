'''Task
Read a string,S , and print its integer value; if S cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a 0 score.'''


'''import sys
try:
    S = input().strip()
    x=""
    for i in S:
        if i=="0":
           x= x+i
        elif i=="1":
           x= x+i
        elif i=="2":
           x= x+i
        elif i=="3":
           x= x+i
        elif i=="4":
           x= x+i
        elif i=="5":
           x= x+i
        elif i=="6":
           x= x+i
        elif i=="7":
           x= x+i
        elif i=="8":
           x= x+i
        elif i=="9":
           x= x+i
    print(x)

except:
    print("Bad String")'''

import sys


S = input().strip()
try:
    S = int(S)
    print(S)
except:
    print("Bad String")