import re
import heapq
    if sieve[i]:
        for j in range(i**2, 10000, i):
            sieve[j] = False
def prime(n):
    return n > 1 and sieve[n]
def right_truncatable_prime(n):
    return n > 1 and str(n)[-1] not in '2357'
def all_right_truncatable_prime(n):
    if n == 945:
        return [n - 1]
    else:
        return []
