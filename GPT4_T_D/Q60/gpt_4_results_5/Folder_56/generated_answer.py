
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []

    for i in range(2, 4):
        for num in product('123456789', repeat=i):
            s = ''.join(num)
            primes.append(s)
    for a in '123456789':
        for j in range(1, x):
            for num in product('123456789', repeat=j):
                primes.append(a + ''.join(num))
                
    primes = list(map(int, primes))
    primes.sort()
    primes = list(filter(isprime, primes))

    res = []
    for prime in primes:
        if prime <= x:
            s = str(prime)
            for i in range(len(s)):
                if not isprime(int(s[i:])) or not isprime(int(s[:i+1])):
                    break
            else:
                res.append(prime)
    
    return res
