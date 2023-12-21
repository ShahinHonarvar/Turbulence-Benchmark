
from itertools import product
import math

def all_left_right_truncatable_prime(t):
    x = t[65]
    primes = []

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, math.isqrt(n) + 1, 2):
            if n % current == 0: 
                return False
        return True

    def check_truncations(num):
        if '0' in num:
            return False
        for i in range(len(num)):
            left_trunc = num[i:]
            right_trunc = num[:len(num)-i]
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                return False
        return True

    num_list = [i for i in range(1, x+1) if is_prime(i)]
    for num in num_list:
        if check_truncations(str(num)):
            primes.append(num)
            
    primes.sort(reverse=True)
    return primes
