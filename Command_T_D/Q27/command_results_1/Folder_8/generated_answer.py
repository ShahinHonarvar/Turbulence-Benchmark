
import bisect

def insert_after_index(lst):
    return lst[:bisect.bisect_left(lst, 76)] + [76] + lst[bisect.bisect_left(lst, 76):]
