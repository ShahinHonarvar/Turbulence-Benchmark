
import math

def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[100]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            is_truncatable_prime = True
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(num)

    return sorted(truncatable_primes)
