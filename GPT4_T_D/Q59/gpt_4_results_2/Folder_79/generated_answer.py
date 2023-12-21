
from itertools import combinations 

def all_left_truncatable_prime(tup):
    x = tup[91]
    primes = [2]
    truncatable_primes = []
    for num in range(3, x, 2):
        for i in primes:
            if num % i == 0:
                break
        else:
            primes.append(num)
    for prime in primes:
        if '0' in str(prime):
            continue
        points = len(str(prime))
        if all(int(''.join(map(str, str(prime)[i: points]))) in primes for i in range(points)): 
            truncatable_primes.append(prime)
    return truncatable_primes
