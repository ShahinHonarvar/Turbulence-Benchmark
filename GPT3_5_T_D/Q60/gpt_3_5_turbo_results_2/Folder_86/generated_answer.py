
import math

def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        digits = str(n)
        if '0' in digits:
            return False
        length = len(digits)
        for i in range(length):
            if not is_prime(int(digits[i:])):
                return False
            if not is_prime(int(digits[:length-i])):
                return False
        return True
    
    x = numbers[126]
    trun_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            trun_primes.append(i)
    return sorted(trun_primes, reverse=True)
