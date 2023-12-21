from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[22:24 + 1]
    return sum([i for i in l if i % -85 == 0 or i % -30 == 0])
