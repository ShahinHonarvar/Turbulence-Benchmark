
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[89]
    primes = []
    for num in range(13, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        prime = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                prime = False
                break
        if prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
