
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for num in range(2, x):
        if isprime(num):
            num_str = str(num)
            is_right_truncatable = True
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[:-i])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes)
