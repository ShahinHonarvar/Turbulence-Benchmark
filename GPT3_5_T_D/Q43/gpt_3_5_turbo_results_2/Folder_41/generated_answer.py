
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [num for num in lst[45:81] if is_prime(num)]
    primes.sort(reverse=True)
    return primes
