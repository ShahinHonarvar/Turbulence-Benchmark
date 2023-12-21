
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for num in range(11, x + 1, 2):
        is_lr_truncable = True
        if '0' in str(num):
            continue

        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:len(str(num))-i])):
                is_lr_truncable = False
                break
        
        if is_lr_truncable:
            primes.append(num)
    primes.sort()        
    return primes
