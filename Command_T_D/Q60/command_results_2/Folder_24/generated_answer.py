
import itertools

def all_left_right_truncatable_prime(range_):
    result = list(itertools.filterfalse(lambda x: (x > 1) and (x < range_[0]) and (str(x) in str(range_[0])), range_[0]))
    return result
