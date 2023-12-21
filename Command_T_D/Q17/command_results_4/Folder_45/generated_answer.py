
import bisect

def all_ints_div_by_both_two_nums(ints):
    return [int(i) for i in ints[bisect.bisect_left(ints, 30):bisect.bisect_right(ints, 200)]]
