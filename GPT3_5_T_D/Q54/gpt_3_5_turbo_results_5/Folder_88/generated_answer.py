
import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[93]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            prime = True
            num = i
            while num > 0:
                if not is_prime(num):
                    prime = False
                    break
                num //= 10
            if prime:
                primes.append(i)
    return sorted(primes)
