from typing import List


def all_ints_div_by_both_two_nums(l: List[int]) -> List[int]:
    l = l[55:66 + 1]
    return [i for i in l if i % 22 == 0 and i % 82 == 0]
