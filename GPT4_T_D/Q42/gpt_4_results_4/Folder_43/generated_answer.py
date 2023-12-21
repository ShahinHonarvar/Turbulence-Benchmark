
from sympy import primefactors

def prime_factors(numbers):
    try:
        return set(primefactors(numbers[29]))
    except IndexError:
        return "Index out of range"
