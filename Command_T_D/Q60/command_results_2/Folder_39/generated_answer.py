
import sys

def all_left_right_truncatable_prime(x_list):
    #sys.setrecursionlimit(10**5)
    #sys.setrecursionlimit(1_000_000)
    x = x_list[30]
    #x = 1_000_000
    #sys.setrecursionlimit(1_000_000)
    left_right_truncatable_primes = []
    for prime in range(2, x + 1):
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    prime = True
    for c in range(1, len(n_str)):
        if n_str[c] == '0':
            prime = False
            break
        if n_str[0] == '0':
            prime = False
            break
        if n_str[len(n_str) - 1] == '0':
            prime = False
            break
        if n_str[0] == '1' and n_str[c] == '1':
            prime = False
            break
        if n_str[len(n_str) - 1] == '9' and n_str[c] == '9':
            prime = False
            break
        if n_str[0] == '2' and n_str[c] == '2':
            prime = False
            break
    return prime
