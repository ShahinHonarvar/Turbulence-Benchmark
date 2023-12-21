
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[35]
    desc_ordered_r_primes = []
    for num in range(x):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                break
        else:
            desc_ordered_r_primes.append(num)
    desc_ordered_r_primes.sort(reverse=True)
    return desc_ordered_r_primes
