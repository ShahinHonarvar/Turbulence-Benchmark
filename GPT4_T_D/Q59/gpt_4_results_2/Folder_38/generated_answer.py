
from itertools import permutations
from sympy import isprime

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[28]
    
    primes_list = ['2', '3', '5', '7']
    left_truncatable_primes = []

    while len(primes_list) > 0:
        new_primes_list = []
        for p_str in primes_list:
            for ch in '123456789':
                new_number = int(p_str + ch)
                if new_number < x and isprime(new_number):
                    new_primes_list.append(p_str + ch)
        primes_list = new_primes_list
        left_truncatable_primes += primes_list

    ltp_ints = list(map(int, left_truncatable_primes))
    ltp_ints.sort()
    
    return ltp_ints
