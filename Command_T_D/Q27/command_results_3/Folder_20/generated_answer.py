
import bisect

def insert_after_index(s):
    ins = [54, 96]
    bisect.insort(s, ins)
    return s + ins
