
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 23:
            continue
        str_x = str(x)
        prime = True
        for i in range(len(str_x)):
            if str_x[i] == "0":
                prime = False
                break
            if not is_prime(int(str_x[i:])):
                prime = False
                break
            if not is_prime(int(str_x[:len(str_x)-i])):
                prime = False
                break
        if prime:
            primes.append(x)
    return sorted(primes)
