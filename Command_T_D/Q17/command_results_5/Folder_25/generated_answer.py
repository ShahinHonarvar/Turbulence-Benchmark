
import bisect

def all_ints_div_by_both_two_nums(a):
    i = bisect.bisect_left(a, -20)
    j = bisect.bisect_left(a, -26)
    if i >= 25 and j <= 80:
        return a[i:j+1]
    else:
        return []
