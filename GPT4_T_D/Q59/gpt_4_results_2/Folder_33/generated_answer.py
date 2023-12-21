
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[945]
    left_trunc_primes = []
    for i in range(10, x):
        num = str(i)
        if '0' in num:
            continue
        else:
            for j in range(len(num)):
                cut_num = int(num[j:])
                if not isprime(cut_num):
                    break
            else:
                left_trunc_primes.append(i)
    return sorted(left_trunc_primes, reverse=True)
