
import math

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[41]

    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def isTruncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not(isPrime(int(str_n[i:])) and isPrime(int(str_n[:i+1]))):
                return False
        return True

    truncatable_primes = []
    for i in range(1, x + 1):
        if isTruncatable(i):
            truncatable_primes.append(i)

    truncatable_primes.sort()

    return truncatable_primes
