
import bisect

def all_ints_div_by_both_two_nums(a):
    result = []
    i = bisect.bisect_left(a, -2)
    j = bisect.bisect_left(a, 3)
    while i < j:
        if a[i] % -2 == 0 and a[i] % 3 == 0:
            result.append(a[i])
        i += 1
    return result
