
import itertools

def all_ints_div_by_both_two_nums(x):
    return [x[i] for i in range(40, 200) if (x[i]%71 == 0 and x[i]%21 == 0)]
