
import math

def prime_factors(lst):
    num = lst[38]
    factors = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.add(i)
            num = num / i
    if num > 1:
        factors.add(num)
    return factors
