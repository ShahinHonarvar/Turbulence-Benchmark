
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[177]
    right_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        prime = True
        while prime and str_num:
            prime = isprime(int(str_num))
            str_num = str_num[:-1]
        if prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
