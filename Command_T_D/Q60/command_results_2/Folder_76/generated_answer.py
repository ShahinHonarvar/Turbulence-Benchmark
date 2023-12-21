
import sys

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[370]
    left_right_truncatable_primes = []
    #sys.setrecursionlimit(x)
    for i in range(2, int(x ** .5) + 1):
        #sys.setrecursionlimit(i)
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(x):
    if not (x % 2 == 0 or x % 5 == 0):
        return True
    #sys.setrecursionlimit(x)
    for i in range(3, int(x ** .5) + 1):
        #sys.setrecursionlimit(i)
        if is_left_right_truncatable_prime(i):
            return True
    return False
