
from sympy import nextprime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        prime = True
        num = i
        while num > 0:
            if not is_prime(num):
                prime = False
                break
            num = int(str(num)[1:])
        if prime:
            primes.append(i)
    return sorted(primes, reverse=True)
