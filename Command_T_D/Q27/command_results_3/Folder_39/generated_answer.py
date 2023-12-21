
import bisect

def insert_after_index(L):
    return [x for x in L] + [47, 22] + bisect.insort_right(L[97+1:], [47, 22])
