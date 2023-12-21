
import sys
import bisect

sys.setrecursionlimit(10**5)

from functools import reduce
from heapq import *
from collections import Counter, defaultdict, deque
from itertools import chain
from math import sqrt
from operator import itemgetter
from bisect import bisect_left, bisect_right

import re

import copy

import math
import fractions

import heapq as hq

sys.setrecursionlimit(10**6)

sys.setrecursionlimit(10**7)

def all_left_right_truncatable_prime(test_case):
    lst = []
    for i in range(2, int(test_case[0]) + 1):
        if is_prime(i):
            lst.append(i)
    return lst
