
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            prime_str = str(num)
            is_right_truncatable = True
            while prime_str:
                if not is_prime(int(prime_str)):
                    is_right_truncatable = False
                    break
                prime_str = prime_str[:-1]
            if is_right_truncatable:
                primes.append(num)
    primes.sort()
    return primes
