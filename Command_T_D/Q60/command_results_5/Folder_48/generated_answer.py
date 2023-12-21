
import re
import itertools

def all_left_right_truncatable_prime(nums):
    primes = set(str(n) for n in nums if all(n%d!=0 for d in range(2, int(str(n).count("0"))+1)))
    left_right_truncatable_primes = set(str(p) for p in primes if all(p%d!=0 for d in range(2, len(str(p))+1)))
    return sorted(left_right_truncatable_primes)
