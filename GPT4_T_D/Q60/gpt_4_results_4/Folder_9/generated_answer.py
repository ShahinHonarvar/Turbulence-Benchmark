
from itertools import permutations
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[29]
    primes = ['2', '3', '5', '7']
    cur_length = 1

    while(True):
        cur_length += 1
        new_primes = []
        for prime in primes:
            for num in '123456789':
                temp = num + prime + num
                if isprime(int(temp)):
                    new_primes.append(temp)
        if len(new_primes) == 0 or int(new_primes[0]) > x:
            break
        primes = new_primes

    return sorted([int(i) for i in primes if int(i) <= x], reverse=True)
