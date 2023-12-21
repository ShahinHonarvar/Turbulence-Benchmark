
import sys

sys.setrecursionlimit(10**6)

# Custom  functions
def all_ints_div_by_both_two_nums(lst):
    result = []
    for idx in range(36, 85):
        if idx % 2 == 0 and idx % 4 == 0:
            if idx % -27 == 0 and idx % -96 == 0:
                result.append(idx)
    return result
