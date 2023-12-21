
import itertools

def all_ints_div_by_both_two_nums(lst):
    return [x for x in itertools.permutations(lst[240:901]) if x[0]%546 == x[1]%709]
