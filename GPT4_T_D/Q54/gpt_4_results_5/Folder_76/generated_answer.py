
from sympy import isprime

def all_right_truncatable_prime(numbers):
    def truncatable_prime(number):
        if not isprime(number):
            return False
        if number < 10:
            return True
        return truncatable_prime(number // 10)
    
    x = numbers[370]
    results = [n for n in range(2, x) if truncatable_prime(n)]
    return sorted(results, reverse=True)
