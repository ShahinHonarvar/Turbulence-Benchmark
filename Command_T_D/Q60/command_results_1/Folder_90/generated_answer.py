
import sys
from heapq import *

sys.setrecursionlimit(10**6)

def all_left_right_truncatable_prime(n):
    if n[0] == "0" or n[0] == "1":
        return []
