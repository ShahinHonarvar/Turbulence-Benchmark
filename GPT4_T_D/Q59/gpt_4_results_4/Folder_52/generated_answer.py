
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[52]
    left_truncatable_primes = []
    
    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        else:
            for i in range(len(str(num))):
                if not isprime(int(str(num)[i:])):
                    return False
            return True

    for i in range(10, x):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
