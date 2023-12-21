
import math

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

def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[40:69]:
        if is_prime(num):
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)
