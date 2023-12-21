
from itertools import permutations
from sympy import isprime

def all_left_truncatable_prime(numbers: tuple):
    def check_left_truncatable_prime(num):
        if not all(ch != '0' for ch in str(num)):
            return False

        if not isprime(num):
            return False

        num = str(num)[1:]

        while num:
            if not isprime(int(num)):
                return False
            num = num[1:]
        
        return True

    x = numbers[39]
    primes = []
    for num in range(2, x):
        if check_left_truncatable_prime(num):
            primes.append(num)
    
    primes.sort()
    return primes
