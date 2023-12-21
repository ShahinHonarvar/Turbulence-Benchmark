
import bisect

def insert_after_index(lst):
    idx = bisect.bisect_left(lst, 27)
    if idx == len(lst):
        return lst + [27]
    bisect.insort_left(lst, 27, idx + 1)
    return lst[:idx] + [27] + lst[idx+1:]
