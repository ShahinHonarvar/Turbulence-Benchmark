
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[30]
    trunc_primes = []
    for num in range(10, x):
        if '0' not in str(num) and isprime(num):
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if isprime(int(temp)):
                    if len(temp) == 1:
                        trunc_primes.append(num)
                else:
                    break
    trunc_primes.sort(reverse=True)
    return trunc_primes
