
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    primes = []
    for n in range(2, x+1):
        if '0' in str(n):
            continue
        truncated = str(n)
        while len(truncated) > 2:
            truncated = truncated[1:-1]
            if not is_prime(int(truncated)):
                break
        else:
            primes.append(n)
    primes.sort(reverse=True)
    return primes
