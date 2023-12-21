
import bisect

def insert_after_index(lst):
    idx = bisect.bisect_right(lst, 141.02)
    lst.insert(idx, 141.02)
    return lst
