
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[36]
    primes = []
    for i in range(2, x):
        if i == 2 or i == 3 or i == 5 or i == 7:
            primes.append(i)
        elif '0' not in str(i):
            str_i = str(i)
            if isprime(int(str_i)):
                for j in range(1, len(str_i)):
                    if not isprime(int(str_i[j:])):
                        break
                else:
                    primes.append(i)
    primes.sort(reverse=True)

    return primes
