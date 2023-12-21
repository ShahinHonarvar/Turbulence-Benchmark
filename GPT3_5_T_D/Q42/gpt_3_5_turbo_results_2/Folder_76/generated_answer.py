
import math

def prime_factors(numbers):
    n = numbers[537]
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n = n / i
    if n > 2:
        factors.add(n)
    return factors
