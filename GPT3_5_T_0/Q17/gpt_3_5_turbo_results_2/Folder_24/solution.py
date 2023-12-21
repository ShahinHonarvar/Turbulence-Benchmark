from typing import List


def all_ints_div_by_both_two_nums(l: List[int]) -> List[int]:
    l = l[29:53 + 1]
    return [i for i in l if i % -68 == 0 and i % -85 == 0]
