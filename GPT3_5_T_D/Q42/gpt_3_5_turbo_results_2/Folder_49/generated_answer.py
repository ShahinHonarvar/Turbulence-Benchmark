
import math

def prime_factors(lst):
    number = lst[68]
    factors = set()

    if number < 2:
        return factors

    while number % 2 == 0:
        factors.add(2)
        number //= 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.add(i)
            number //= i

    if number > 2:
        factors.add(number)

    return factors
