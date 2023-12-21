
from sympy import isprime

def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[86]
    left_truncatable_primes = []
    for num in range(11, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        while len(num_str) > 0:
            if isprime(int(num_str)):
                num_str = num_str[1:]
                if len(num_str) == 0:
                    left_truncatable_primes.append(num)
            else:
                break
    return sorted(left_truncatable_primes)
