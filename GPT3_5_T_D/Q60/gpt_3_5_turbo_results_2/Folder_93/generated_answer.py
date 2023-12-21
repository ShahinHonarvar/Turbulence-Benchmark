
import math

def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return True

    x = numbers[11]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)
