
import bisect

def all_ints_div_by_both_two_nums(lst):
    x, y = bisect.bisect_left(lst, (73, 0)), bisect.bisect_right(lst, (86, 1))
    return lst[x:y]
