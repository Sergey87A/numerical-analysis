
# A python program to approximate a root of a polynomial
# using the newton-raphson method
import math
# f(x) - the function of the polynomial

def f(x):
    function = (x * x * x) - (2 * x) - 1
    return function

def derivative(x):  # function to find the derivative of the polynomial
    h = 0.000001
    derivative = (f(x + h) - f(x)) / h
    return derivative



def newton_raphson(x):
    return (x - (f(x) / derivative(x)))

# p - the initial point i.e. a value closer to the root
# n - number of iterations


def iterate(p, n):
    x = p
    for _ in range(n):
        x = newton_raphson(x)
    return x


print (iterate(1, 5))
# print the root of the polynomial x^3 - 2x - 1 using 3 iterations and taking initial point as 1
