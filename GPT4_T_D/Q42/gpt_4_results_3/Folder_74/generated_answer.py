
import math

def prime_factors(numbers):
    def factors(n):
        i = 2
        factors_set = set()
        while i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors_set.add(i)
        return factors_set

    try:
        return factors(numbers[48])
    except IndexError:
        return "List is shorter than 49 elements."
