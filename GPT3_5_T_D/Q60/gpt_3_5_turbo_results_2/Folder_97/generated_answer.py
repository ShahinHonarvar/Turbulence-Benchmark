
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[645]
    left_right_truncatable_primes = []
    for num in range(2, x+1):
        if is_prime(num):
            prime_str = str(num)
            if '0' not in prime_str:
                is_left_right_truncatable = True
                for i in range(1, len(prime_str)):
                    if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:len(prime_str)-i])):
                        is_left_right_truncatable = False
                        break
                if is_left_right_truncatable:
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)
