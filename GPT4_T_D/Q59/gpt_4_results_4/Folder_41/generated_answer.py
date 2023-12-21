
from sympy import isprime

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[46]
    primes = []
    
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    
    return primes
