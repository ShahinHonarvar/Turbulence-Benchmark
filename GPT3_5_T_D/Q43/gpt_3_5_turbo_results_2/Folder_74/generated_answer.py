
import math

def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
      
    primes = []
    
    for num in lst[23:76]:
        if is_prime(num):
            primes.append(num)
    
    primes.sort(reverse=True)
    
    return primes
