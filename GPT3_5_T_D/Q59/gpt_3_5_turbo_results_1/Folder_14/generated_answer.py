
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    primes = []
    for i in range(2, x):
        num_str = str(i)
        if '0' not in num_str:
            is_truncatable_prime = True
            for j in range(len(num_str)):
                trunc_num = int(num_str[j:])
                if not is_prime(trunc_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(i)

    return sorted(primes, reverse=True)
