
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = []

    def check_prime(n):
        if not isprime(n):
            return False
        else:
            return True
    
    def truncatable(n):
        str_n = str(n)
        if "0" in str_n:
            return False
        for i in range(len(str_n)):
            if not check_prime(int(str_n[i:])) or not check_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    for i in range(10, x + 1):
        if truncatable(i):
            primes.append(i)

    return sorted(primes)
