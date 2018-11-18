
def Samesign(a, b):
    return a * b > 0

def Bisect(func, low, high):
    'Find root of continuous function where f(low) and f(high) have opposite signs'

    if not Samesign(func(low), func(high)):
        for i in range(54): #N=54
            midpoint = (low + high) / 2.0
            if Samesign(func(low), func(midpoint)):
                low = midpoint
            else:
                high = midpoint
        return midpoint
    else:
        return "the function has no roots"

def f(x):
        return 2*x**2-4*x+8
x = Bisect(f,-5, 0)
print(x)