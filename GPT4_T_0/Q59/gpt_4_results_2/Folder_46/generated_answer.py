
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[33]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            temp = str(num)
            while len(temp) > 0:
                if isprime(int(temp)):
                    temp = temp[1:]
                else:
                    break
            if len(temp) == 0:
                primes.append(num)
    return sorted(primes)
