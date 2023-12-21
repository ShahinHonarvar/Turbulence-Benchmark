
import sys
from functools import reduce
from operator import mul
from collections import defaultdict
from heapq import *
from bisect import bisect_left as bl, bisect_right as br
from itertools import permutations
from fractions import Fraction as f
from math import sqrt, gcd
from copy import *

sys.setrecursionlimit(10**6)
mod = 10**9+7
INF = 10**18
eps = 1.0 / 10**10
mod = 998244353


def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d, r = 5, 6
    while d <= int(n ** .5):
        if n % d == 0:
            return False
        d += r
        r = 6 - r
    return True


def prime_list(n):
    #Your code here
    if n <= 1:
        return []
    if n <= 3:
        return [2, 3]
    if n % 2 == 0 or n % 3 == 0:
        return []
    d, r = 5, 6
    while d <= int(n ** .5):
        if n % d == 0:
            return []
        d += r
        r = 6 - r
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 409, 419, 421, 431, 439, 443, 449, 457, 461, 463, 467, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 637, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 693, 719, 733, 751, 757, 761, 763, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 833, 839, 853, 857, 859, 863, 867, 871, 873, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 991, 997]
