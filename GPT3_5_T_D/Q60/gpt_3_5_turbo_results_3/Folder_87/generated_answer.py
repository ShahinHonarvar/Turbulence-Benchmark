
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    while len(str(n)) > 2:
        if not is_prime(n):
            return False
        n = int(str(n)[1:-1])
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    results = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            results.append(i)
    return sorted(results, reverse=True)
