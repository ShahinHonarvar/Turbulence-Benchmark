import bisect
import functools
import heapq
import math
import re
import sys
import time
import collections
import fractions
import itertools
import operator
import random
import bisect
import functools
import heapq
import math
import re
import sys
import time
import collections
import fractions
import itertools
import operator
import random
def all_left_truncatable_prime(test_list):
    res = []
    for i in range(2, test_list[0]):
        temp = []
        for j in range(i, test_list[0], i):
            if is_left_truncatable_prime(j):
                temp.append(j)
        if len(temp) > 0:
            res += temp
    return res
def is_left_truncatable_prime(x):
    s = str(x)
    if len(s) == 0:
        return False
    if s[0] == "0":
        return False
    i = 1
    while i < len(s):
        if s[i] == "0":
            return False
        i += 1
    return True
