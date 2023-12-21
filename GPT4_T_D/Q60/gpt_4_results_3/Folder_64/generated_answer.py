
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[4]
    primes = []
    
    def is_left_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not (isprime(int(n_str[i:])) and isprime(int(n_str[:len(n_str)-i]))):
                return False
        return True

    for i in range(11, x+1):
        if '0' not in str(i) and is_left_right_truncatable(i):
            primes.append(i)
    return sorted(primes)
