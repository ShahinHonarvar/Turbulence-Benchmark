
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = []

    for n in range(10, x+1):
        if '0' in str(n):
            continue
        
        number = str(n)
        truncatable = True

        for i in range(1, len(number)):
            if not isprime(int(number[i:])) or not isprime(int(number[:-i])):
                truncatable = False
                break
        
        if truncatable and isprime(int(number)):
            truncatable_primes.append(n)
    
    return sorted(truncatable_primes, reverse=True)
