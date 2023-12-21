
from sympy import isprime

def all_left_truncatable_prime(tpl):
    x = tpl[86]
    primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        numbers = [int(str(i)[j:]) for j in range(len(str(i)))]
        if all(isprime(num) for num in numbers):
            primes.append(i)
    return sorted(primes, reverse=True)
