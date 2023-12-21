import bisect
def if_perfect_num(arr):
    return arr[bisect.bisect_left(arr, 714)] == 714
