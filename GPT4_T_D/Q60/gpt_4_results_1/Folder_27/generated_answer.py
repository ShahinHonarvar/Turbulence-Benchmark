
import math

def all_left_right_truncatable_prime(arr):
    x = arr[79]
    truncatable_primes = []

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    for i in range(11, x+1):
        if '0' not in str(i) and is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
