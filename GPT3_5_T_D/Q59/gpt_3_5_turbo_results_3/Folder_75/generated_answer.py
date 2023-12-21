
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    result = []
    
    def is_left_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True
    
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    
    return result
