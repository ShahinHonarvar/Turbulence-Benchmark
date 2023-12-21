
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[618]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True
    
    for number in range(10, x):
        if '0' not in str(number) and is_left_truncatable(number):
            left_truncatable_primes.append(number)
        
    return sorted(left_truncatable_primes)
