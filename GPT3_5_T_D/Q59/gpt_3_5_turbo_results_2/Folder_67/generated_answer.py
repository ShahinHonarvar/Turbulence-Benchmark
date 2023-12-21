
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

def all_left_truncatable_prime(numbers):
    x = numbers[71]
    primes = []
    for i in range(10, x):
        prime = True
        str_num = str(i)
        for j in range(1, len(str_num)):
            if not is_prime(int(str_num[j:])):
                prime = False
                break
        if prime:
            primes.append(i)
    return sorted(primes, reverse=True)
