
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[46]
    truncatable_primes = []
    
    def is_truncatable_prime(number):
        number_str = str(number)
        if '0' in number_str:
            return False
        
        while len(number_str) > 1:
            if not isprime(int(number_str)):
                return False
            number_str = number_str[1:-1]
        
        return True
    
    for number in range(2, x+1):
        if is_truncatable_prime(number):
            truncatable_primes.append(number)
    
    return sorted(truncatable_primes, reverse=True)
