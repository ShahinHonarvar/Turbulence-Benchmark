
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]

    def is_left_trunc_prime(n):
        s = str(n)
        return '0' not in s and all(isprime(int(s[i:])) for i in range(len(s)))
    
    return sorted(filter(is_left_trunc_prime, range(2, x)))
