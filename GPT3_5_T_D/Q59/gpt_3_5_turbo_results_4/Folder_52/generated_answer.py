
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[52]
    primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_truncatable = True
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_truncatable = False
                    break
                temp_num = int(str(temp_num)[1:])
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
