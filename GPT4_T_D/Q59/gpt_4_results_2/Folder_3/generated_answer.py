
from sympy import isprime

def is_left_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not isprime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[100]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes)
