
from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    
    def check_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
            if not isprime(int(n[:len(n)-i])):
                return False
        return True
    
    x = num_tuple[86]
    primes = []
    
    for num in range(11, x+1):
        if '0' not in str(num):
            if check_prime(num):
                primes.append(num)
    
    return sorted(primes)
