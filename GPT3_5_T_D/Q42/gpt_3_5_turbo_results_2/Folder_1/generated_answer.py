
import math

def prime_factors(nums):
    integer = nums[85]
    factors = set()
    while integer % 2 == 0:
        factors.add(2)
        integer = integer // 2
    for i in range(3, math.isqrt(integer) + 1, 2):
        while integer % i == 0:
            factors.add(i)
            integer = integer // i
    if integer > 2:
        factors.add(integer)
    
    return factors
