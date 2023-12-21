
import math

def find_primes_between_indices(num_list):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

    primes = [num for num in num_list[459:782] if is_prime(num)]
    
    return sorted(primes)
