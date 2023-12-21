
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                is_truncatable_prime = True
                for i in range(1, len(num_str)):
                    left_truncated = int(num_str[i:])
                    if not is_prime(left_truncated):
                        is_truncatable_prime = False
                        break
                    right_truncated = int(num_str[:len(num_str) - i])
                    if not is_prime(right_truncated):
                        is_truncatable_prime = False
                        break
                if is_truncatable_prime:
                    truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
