
import math

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

def all_right_truncatable_prime(numbers):
    x = numbers[10]
    truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = str(num)
            is_truncatable_prime = True
            for i in range(1, len(temp)):
                if not is_prime(int(temp[:i])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
