
import math

def prime_factors(numbers):
    integer = numbers[478]
    factors = set()
    for i in range(2, int(math.sqrt(integer)) + 1):
        while integer % i == 0:
            factors.add(i)
            integer /= i
    if integer > 1:
        factors.add(integer)
    return factors
