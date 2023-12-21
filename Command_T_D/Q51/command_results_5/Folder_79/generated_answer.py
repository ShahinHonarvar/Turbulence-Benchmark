import sys
import functools
import bisect
import heapq
@functools.lru_cache(maxsize=1_000_000)
def if_contains_anagrams(s):
    return len(s) <= 173 and all(s[bisect.bisect_left(s, s[i])] == s[i] for i in range(len(s) - 2))
