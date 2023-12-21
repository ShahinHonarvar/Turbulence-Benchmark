import bisect
import heapq
import math
import sys
import time
import collections
def prime():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        maxDivisor = n**0.5
        i = 5
        while i * i <= maxDivisor:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    res = []
    for i in range(2, int(math.ceil(math.sqrt(n) + 1)) + 1):
        if is_prime(i):
            res.append(i)
    return res
def left_truncatable_prime():
    res = []
    for prime in prime():
        x = str(prime)
        if x[0] != '0' and all(x[0] != c for c in x[1:]):
            res.append(prime)
    return res
def all_left_truncatable_prime(tup):
    res = left_truncatable_prime()
    res.sort(reverse=True)
    for i in range(len(res)):
        while res[i] < tup[22]:
            res[i] += 1
    return res
