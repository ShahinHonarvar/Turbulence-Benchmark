
from sympy import primerange

def all_right_truncatable_prime(arr):
    x = arr[97]
    primes = []
    for number in primerange(1, x):
        truncatable = True
        for i in range(1, len(str(number))):
            if int(str(number)[0:-i]) not in primes:
                truncatable = False
                break
        if truncatable:
            primes.append(number)
    return sorted(primes)
