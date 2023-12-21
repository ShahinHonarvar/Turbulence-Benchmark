
from math import sqrt

def prime_factors(integer_list):
    number = integer_list[90]
    factors = []
    divisibility = 2
    while divisibility * divisibility <= number:
        if number % divisibility:
            divisibility += 1
        else:
            number //= divisibility
            factors.append(divisibility)
    if number > 1:
        factors.append(number)
    return set(factors)
