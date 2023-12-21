
import math

def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(14, 74):
        if is_prime(lst[i]):
            primes.append(lst[i])
    
    return sorted(primes, reverse=True)
