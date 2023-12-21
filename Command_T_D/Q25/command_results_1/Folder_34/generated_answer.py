
import bisect

def insert_at_index(lst):
    ins = bisect.insort_left(lst, 783.25)
    return ins + lst
