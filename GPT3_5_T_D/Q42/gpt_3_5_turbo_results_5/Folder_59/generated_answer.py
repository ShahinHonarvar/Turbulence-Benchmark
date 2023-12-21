
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    integer_at_index_2 = numbers[2]
    factors = set()
    for i in range(2, integer_at_index_2 + 1):
        if integer_at_index_2 % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors
