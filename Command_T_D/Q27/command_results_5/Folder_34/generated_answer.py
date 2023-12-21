
import bisect

def insert_after_index(lst):
    bisect.insort_right(lst, 783.25)
    return lst[:-1] + [783.25] + lst[bisect.bisect_right(lst, 783.25):]
