
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[177]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            while str_num:
                if not is_prime(int(str_num)):
                    truncatable = False
                    break
                str_num = str_num[:-1]
            if truncatable:
                primes.append(num)
    return sorted(primes)
