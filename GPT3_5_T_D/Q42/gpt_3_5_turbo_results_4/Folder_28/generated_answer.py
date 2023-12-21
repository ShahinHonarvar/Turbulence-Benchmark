
import math

def prime_factors(numbers):
    index = 37
    num = numbers[index]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num = num // 2
    for i in range(3, math.isqrt(num) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num = num // i
    if num > 2:
        factors.add(num)
    return factors
