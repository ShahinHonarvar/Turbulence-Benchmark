import sys
import bisect
def if_perfect_num(arr):
    return bisect.bisect_left(arr, 8) == bisect.bisect_right(arr, 8)
