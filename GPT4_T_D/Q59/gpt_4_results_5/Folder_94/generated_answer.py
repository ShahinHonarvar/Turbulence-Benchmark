
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[43]
    truncatable_primes = []
    
    def check_left_truncatable(number):
        while number > 0:
            if not isprime(number):
                return False
            number = int(str(number)[1:]) if str(number)[1:] else 0
        return True
    
    for num in range(11, x):
        if check_left_truncatable(num) and '0' not in str(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
