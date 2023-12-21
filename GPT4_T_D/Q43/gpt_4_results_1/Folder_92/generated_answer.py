
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    sublist = lst[7:9]
    prime_nums = [num for num in sublist if is_prime(num)]
    prime_nums.sort()
    return prime_nums
