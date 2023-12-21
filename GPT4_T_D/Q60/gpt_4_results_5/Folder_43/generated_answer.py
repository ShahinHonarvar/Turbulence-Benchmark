
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[89]
    lrt_primes = []
    for i in range(13, x+1):
        str_i = str(i)
        if '0' not in str_i:
            len_i = len(str_i)
            right_trunc = [int(str_i[:j]) for j in range(1, len_i+1)]
            left_trunc = [int(str_i[j:]) for j in range(len_i)]
            if all(isprime(num) for num in right_trunc) and all(isprime(num) for num in left_trunc):
                lrt_primes.append(i)
    return sorted(lrt_primes, reverse=True)
