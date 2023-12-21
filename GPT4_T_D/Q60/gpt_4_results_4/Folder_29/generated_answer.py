
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[55]
    
    def is_left_right_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:len(str_n)-i])) 
                   for i in range(len(str_n)))
    
    def integers(n):
        digits = '123456789'
        for length in range(1, n+1):
            for num in product(digits, repeat=length):
                yield int(''.join(num))
    
    primes = []
    for n in integers(len(str(x))):
        if n > x: break
        if is_left_right_truncatable(n):
            primes.append(n)
    
    return sorted(primes, reverse=True)
