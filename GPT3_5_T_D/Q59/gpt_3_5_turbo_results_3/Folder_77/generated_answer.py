
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    primes = []
    for num in range(2, x):
        if isprime(num):
            prime = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    prime = False
                    break
            if prime:
                primes.append(num)
    return sorted(primes, reverse=True)
