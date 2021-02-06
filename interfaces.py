'''Sample Input

6
Sample Output

I implemented: AdvancedArithmetic
12
Explanation

The integer 6 is evenly divisible by 1,2 3, and 6. Our divisorSum method should return the sum of these numbers, which is 1+2+3+6=12.
'''
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1,n+1):
            if n % i == 0:
                sum += i
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)