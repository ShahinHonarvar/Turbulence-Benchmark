
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[84]
    primes = []
    i = 1
    while i < x:
        if is_prime(i):
            primes.append(i)
        i += 1

    right_truncatable_primes = []
    for prime in primes:
        num = prime
        flag = True
        while num > 0:
            if not is_prime(num):
                flag = False
                break
            num //= 10
        if flag:
            right_truncatable_primes.append(prime)

    return sorted(right_truncatable_primes, reverse=True)
