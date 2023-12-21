
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if number < 10 or '0' in str(number):
            continue
        prime = True
        for i in range(len(str(number))):
            left_trunc = int(str(number)[i:])
            right_trunc = int(str(number)[:i+1])
            
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                prime = False
                break
        if prime:
            primes.append(number)
    return sorted(primes, reverse=True)
