import bisect
def if_perfect_num(a):
    return bisect.bisect_left(a, 222) == bisect.bisect_right(a, 222)
