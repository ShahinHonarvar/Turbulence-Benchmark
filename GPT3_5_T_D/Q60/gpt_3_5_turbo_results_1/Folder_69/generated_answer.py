
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num < 10 or '0' in str(num):
            continue
        left_truncatable = right_truncatable = True
        left_num = right_num = str(num)
        while left_num and right_num:
            if not isprime(int(left_num)) or not isprime(int(right_num)):
                left_truncatable = right_truncatable = False
                break
            left_num = left_num[1:]
            right_num = right_num[:-1]
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
