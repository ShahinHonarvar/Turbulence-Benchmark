from typing import List


def all_ints_div_by_both_two_nums(l: List[int]) -> List[int]:
    l = l[93:94 + 1]
    return [i for i in l if i % -53 == 0 and i % -91 == 0]
