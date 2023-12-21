
import math

def prime_factors(num_list):
    num = num_list[8]
    factors = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        while (num % i == 0):
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors
