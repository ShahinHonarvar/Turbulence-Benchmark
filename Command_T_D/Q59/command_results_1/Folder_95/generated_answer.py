import itertools
import re
import bisect
import heapq
import collections
def all_left_truncatable_prime(test_case):
    x = test_case[77]
    left_truncatable_primes = []
    for l in range(1, x + 1):
        for p in itertools.permutations(str(l)):
            if len(p) == 1:
                continue
            elif re.match(r'0+', p):
                continue
            elif all(int(p[0] + i) > l for i in range(1, len(p))):
                if all(isPrime(int(p[i])) for i in range(1, len(p))):
                    left_truncatable_primes.append(int(p[0] + '0'))
        if len(left_truncatable_primes) > test_case[11]:
            break
    return left_truncatable_primes
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = int(n**0.5) + 1
    i = 5
    while i * i <= maxDivisor:
        if n % i == 0:
            return False
        i += 6
    return True
