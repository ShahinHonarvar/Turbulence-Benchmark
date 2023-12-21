import functools
import heapq
@functools.lru_cache(maxsize=10**5)
def gcf_two_nums(lst):
    heapq.heapify(lst)
    i = lst.index(min(lst))
    x = lst[i]
    heapq.heapify(lst)
    j = lst.index(max(lst))
    y = lst[j]
    return functools.lru_cache(maxsize=x*y)
