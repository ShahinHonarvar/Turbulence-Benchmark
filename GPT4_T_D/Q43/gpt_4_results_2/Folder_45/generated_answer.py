
from typing import List

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers: List[int]) -> List[int]:
    primes = []
    for i in range(23, 40):
        try:
            if is_prime(numbers[i]):
                primes.append(numbers[i])
        except IndexError:
            pass
        
    return sorted(primes)
