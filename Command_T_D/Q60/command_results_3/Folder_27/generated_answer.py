
import sys
from collections import *
from functools import *

sys.setrecursionlimit(10**6)
mod = 10**9+7

def all_left_right_truncatable_prime(nums):
    # Your code here.
    l = []
    for i in range(3, len(str(nums[0]))+1):
        for j in range(3, len(str(nums[-1]))+1):
            s = str(nums[0])[:i]+str(nums[-1])[-j:]
            if is_prime(int(s)):
                l.append(int(s))
    return l

def is_prime(n):
    # Your code here.
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    d, r = 5, 2**(n.bit_length()-1)
    while d <= r:
        if n%d == 0:
            return False
        d += 6
    return True
