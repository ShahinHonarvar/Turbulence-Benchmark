from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[93:94 + 1]
    return sum([i for i in l if i % -53 == 0 or i % -91 == 0])
