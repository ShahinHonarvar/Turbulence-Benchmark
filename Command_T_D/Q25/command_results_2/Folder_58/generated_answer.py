
import bisect

def insert_at_index(lst):
    i = bisect.bisect_left(lst, [385, 999])
    lst.insert(i, [385, 999])
    return lst
