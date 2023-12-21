
from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[42]
    trunc_primes = []
    for num in range(13, x+1):
        if '0' in str(num):
            continue
        len_num = len(str(num))
        all_primes_left = all(isprime(int(str(num)[i:])) for i in range(len_num))
        all_primes_right = all(isprime(int(str(num)[:len_num - i])) for i in range(len_num))
        if all_primes_left and all_primes_right:
            trunc_primes.append(num)
    return sorted(trunc_primes)
