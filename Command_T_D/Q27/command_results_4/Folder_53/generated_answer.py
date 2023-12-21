
import bisect

def insert_after_index(lst):
    ins_idx = bisect.bisect_left(lst, (709.87,))
    idx = bisect.bisect_left(lst, (92,))
    lst.insert(ins_idx, (92,))
    lst.insert(idx, (709.87,))
    return lst
