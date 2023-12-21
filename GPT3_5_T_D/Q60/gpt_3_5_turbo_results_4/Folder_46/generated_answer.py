
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

def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            prime_str = str(num)
            is_truncatable = True
            for i in range(len(prime_str)):
                if prime_str[i] == '0':
                    is_truncatable = False
                    break
                if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:i+1])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)
