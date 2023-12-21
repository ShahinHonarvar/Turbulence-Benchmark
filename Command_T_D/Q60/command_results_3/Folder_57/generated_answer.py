
import itertools

def all_left_right_truncatable_prime(test_list):
    res = list(itertools.filterfalse(lambda p: (p in test_list) or (p in test_list) or (p in test_list), list(range(test_list[0], test_list[1]+1))))
    res.sort(reverse=True)
    return res
