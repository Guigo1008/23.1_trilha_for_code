import math

n = 2
somatorio = 0

while n < 100000:
    somatorio = somatorio + 1/2**math.log(n, math.e)
    print(somatorio)
    n = n + 1
