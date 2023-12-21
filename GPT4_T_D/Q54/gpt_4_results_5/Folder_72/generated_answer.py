
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for i in range(2, x):
        str_num = str(i)
        for j in range(len(str_num)):
            if not isprime(int(str_num[j:])):
                break
        else:
            primes.append(i)
    return sorted(primes, reverse=True)
