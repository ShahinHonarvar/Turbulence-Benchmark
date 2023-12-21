
from sympy import primefactors

def prime_factors(list_of_pos_int):
    try:
        return set(primefactors(list_of_pos_int[87]))
    except IndexError:
        return "Error: Index out of range"
