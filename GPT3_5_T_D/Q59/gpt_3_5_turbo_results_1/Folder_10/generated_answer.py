
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_truncatable_primes(n):
    results = []
    for i in range(2, n):
        if is_prime(i):
            truncatable = True
            temp = str(i)
            for j in range(len(temp)):
                if temp[j] == '0':
                    truncatable = False
                    break
                if not is_prime(int(temp[j:])):
                    truncatable = False
                    break
            if truncatable:
                results.append(i)
    return results[::-1]

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    return get_truncatable_primes(x)
