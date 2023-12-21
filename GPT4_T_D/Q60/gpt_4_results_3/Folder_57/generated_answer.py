
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[54]
    lr_truncatable_primes = []
    for i in range(10, x+1):
        if '0' not in str(i):
            ltr_digits = [int(str(i)[:j]) for j in range(1, len(str(i)) + 1)]
            rtl_digits = [int(str(i)[j:]) for j in range(len(str(i)))]
            if all(isprime(n) for n in ltr_digits) and all(isprime(n) for n in rtl_digits):
                lr_truncatable_primes.append(i)
    return sorted(lr_truncatable_primes, reverse=True)
