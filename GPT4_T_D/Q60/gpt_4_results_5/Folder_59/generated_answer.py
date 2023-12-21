
from itertools import product
from sympy import isprime

def number_generator():
    possible_digits = "123456789"
    possible_two_digits = [i + j for i, j in product(possible_digits, repeat=2)]
    possible_set = [i for i in possible_digits] + possible_two_digits

    for length in range(3, 7):
        old_possible_set = possible_set[:]
        for old in old_possible_set:
            possible_set += [old + new for new in possible_digits]
    return possible_set

def truncation_check(number):
    for i in range(len(number)):
        if not isprime(int(number[i:])) or not isprime(int(number[:len(number) - i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    less_than_values = list(filter(lambda x: int(x) <= tup[84], number_generator()))
    truncatable_primes = list(filter(truncation_check, less_than_values))
    truncatable_primes = list(map(int, truncatable_primes))
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
