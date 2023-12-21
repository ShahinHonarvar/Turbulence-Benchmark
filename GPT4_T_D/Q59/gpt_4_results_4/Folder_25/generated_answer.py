
from sympy import isprime

def all_left_truncatable_prime(tuple_vals):
    x = tuple_vals[92]
    primes = []
    
    def is_left_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    for num in range(2, x):
        if isprime(num) and '0' not in str(num) and is_left_truncatable(num):
            primes.append(num)
            
    return sorted(primes)
