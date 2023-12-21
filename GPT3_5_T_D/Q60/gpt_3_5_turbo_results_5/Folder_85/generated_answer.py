
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_left_truncations(n):
    truncations = []
    digits = list(str(n))
    for i in range(len(digits)):
        truncations.append(int(''.join(digits[i:])))
    return truncations

def get_right_truncations(n):
    truncations = []
    digits = list(str(n))
    for i in range(len(digits)):
        truncations.append(int(''.join(digits[:len(digits)-i])))
    return truncations

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            left_truncations = get_left_truncations(num)
            right_truncations = get_right_truncations(num)
            left_right_truncations = set(left_truncations).intersection(right_truncations)
            is_truncatable_prime = True
            for truncation in left_right_truncations:
                if not is_prime(truncation):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(num)
    primes.sort()
    return primes
