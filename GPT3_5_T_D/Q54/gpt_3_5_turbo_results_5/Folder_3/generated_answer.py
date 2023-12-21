
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            truncate_num = num // 10
            is_right_truncatable_prime = True
            while truncate_num > 0:
                if not isprime(truncate_num):
                    is_right_truncatable_prime = False
                    break
                truncate_num //= 10
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
