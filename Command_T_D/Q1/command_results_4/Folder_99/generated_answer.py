
import bisect

def all_ints_inclusive(lst):
    return lst[bisect.bisect_right(lst[:209]+lst[209:556]+lst[556:],0):556]
