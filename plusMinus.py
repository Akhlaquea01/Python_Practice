def plusMinus(arr):
    p=0
    m=0
    n=0
    x=len(arr)
    for i in range (x):
        if (arr[i]>0):
            p=p+1
            
        elif (arr[i]<0):
            m=m+1
        else:
            n=n+1
    pos=p/x
    neg=m/x
    neu=n/x
    pos=round(pos,6)
    neg=round(neg,6)
    neu=round(neu,6)
    print(pos)
    print(neg)
    print(neu)
x = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
