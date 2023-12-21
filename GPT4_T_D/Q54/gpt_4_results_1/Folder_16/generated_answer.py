
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[792]
    right_truncatable_primes = []

    for i in range(2, x):
        number = str(i)
        for j in range(len(number)):
            if not isprime(int(number[j:])):
                break
        else:
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes)
