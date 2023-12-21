
from math import isqrt

def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if n[i] == '0':
                return False
            if not is_prime(int(n[i:])):
                return False
            if not is_prime(int(n[:len(n)-i])):
                return False
        return True

    x = numbers[36]
    truncatable_primes = []
    for num in range(2, x+1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
