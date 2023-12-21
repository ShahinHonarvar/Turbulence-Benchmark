import re
import sys
import functools
import bisect
@functools.lru_cache(maxsize=10**5)
def all_left_truncatable_prime(x):
    if x <= 1:
        return []
    str_x = str(x)
    for i in range(1,len(str_x)-1):
        if str_x[i] == '0':
            continue
        if str_x[0:i] not in '2357':
            continue
        if str_x[i:] not in '2357':
            continue
        str_x = str_x[i:]
    if str_x == '':
        return []
    for i in range(1,len(str_x)-1):
        if str_x[i] == '0':
            continue
        if str_x[0:i] not in '2357':
            continue
        if str_x[i:] not in '2357':
            continue
        str_x = str_x[i:]
    if str_x == '':
        return []
    return [int(str_x)]
