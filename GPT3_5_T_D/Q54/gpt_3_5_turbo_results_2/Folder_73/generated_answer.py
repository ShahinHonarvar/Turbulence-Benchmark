
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            t_num = num
            is_right_truncatable_prime = True
            while t_num > 10:
                t_num = t_num // 10
                if not is_prime(t_num):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
