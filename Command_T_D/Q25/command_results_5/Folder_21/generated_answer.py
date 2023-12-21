
import bisect

def insert_at_index(s):
    return s[:743] + [11.04] + bisect.insort_left(s[743:], 11.04)
