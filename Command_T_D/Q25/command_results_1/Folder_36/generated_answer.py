
import bisect

def insert_at_index(lst):
    idx = bisect.bisect_left(lst, [699, 556])
    insert = [699, 556]
    return lst[:idx] + insert + lst[idx:]+lst[idx+2:]
