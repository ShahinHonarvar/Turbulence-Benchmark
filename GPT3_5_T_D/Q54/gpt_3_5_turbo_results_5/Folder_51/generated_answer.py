
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if n == 0:
        return []
    elif n < 10:
        return [2, 3, 5, 7]
    
    primes = [2, 3, 5, 7]
    results = []
    
    while primes:
        prime = primes.pop()
        digit = 1
        while prime * 10**digit < n:
            new_prime = prime * 10**digit
            for i in range(1, 10):
                if is_prime(new_prime + i):
                    primes.append(new_prime + i)
            if is_prime(new_prime):
                results.append(new_prime)
            digit += 1
    
    return sorted(results)


def all_right_truncatable_prime(numbers):
    x = numbers[54]
    return right_truncatable_prime(x)
