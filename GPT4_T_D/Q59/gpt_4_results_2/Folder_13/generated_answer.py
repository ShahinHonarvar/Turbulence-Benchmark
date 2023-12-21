
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[784]
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)
    
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False

def is_left_truncatable(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True
