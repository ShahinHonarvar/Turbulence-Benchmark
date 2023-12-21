
import math

def prime_factors(integer_list):
    integer = integer_list[40]
    prime_factors = set()
    for i in range(2, int(math.sqrt(integer)) + 1):
        while integer % i == 0:
            prime_factors.add(i)
            integer //= i
    if integer > 1:
        prime_factors.add(integer)
    return prime_factors
