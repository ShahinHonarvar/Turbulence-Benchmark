
from itertools import permutations

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def left_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    primes = [i for i in range(x) if is_prime(i) and left_truncatable(i)]
    return sorted(primes)
