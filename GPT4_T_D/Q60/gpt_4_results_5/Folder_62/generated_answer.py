
from itertools import product

def is_prime(n):
    if n < 2: 
        return False
    if n == 2 or n == 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
    
def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    trunc_primes = [] 
    primes = ['2', '3', '5', '7']
    while len(primes) != 0: 
        prime = primes.pop(0)
        if len(prime) != 1 and int(prime) > x:
            continue
        trunc_primes.append(int(prime))
        for digit in '123456789':
            if is_prime(int(prime + digit)):
                primes.append(prime + digit)
    trunc_primes.sort()
    return trunc_primes
