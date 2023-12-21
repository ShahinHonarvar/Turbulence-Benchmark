
import bisect

def insert_at_index(lst):
    idx = bisect.bisect_left(lst, 10.01)
    lst = lst[:idx] + [10.01] + lst[idx+1:]
    return lst
