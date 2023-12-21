
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[42]
    primes = []
    for i in range(2, x):
        num = str(i)
        if "0" not in num:
            prime = True
            for j in range(len(num)):
                trunc_num = int(num[j:])
                if not isprime(trunc_num):
                    prime = False
                    break
            if prime:
                primes.append(i)
    primes.sort()
    return primes
