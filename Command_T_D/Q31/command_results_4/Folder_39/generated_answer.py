import bisect
def if_perfect_num(a):
    b = sorted(a)
    i = bisect.bisect_left(b, 59)
    return b[i] == 59
