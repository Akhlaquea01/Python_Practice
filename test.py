'''
'''
returnDate, returnMonth, returnYear = [int(x) for x in input().split(' ')]
dueDate, dueMonth, dueYear = [int(x) for x in input().split(' ')]

if (returnYear, returnMonth, returnDate) <= (dueYear, dueMonth, dueDate):
    print(0)
elif (returnYear, returnMonth) == (dueYear, dueMonth):
    print(15 * (returnDate - dueDate))
elif returnYear == dueYear:
    print(500 * (returnMonth - dueMonth))
else:
    print(10000)