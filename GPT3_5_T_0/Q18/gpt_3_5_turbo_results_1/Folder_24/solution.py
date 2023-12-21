from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[29:53 + 1]
    return sum([i for i in l if i % -68 == 0 or i % -85 == 0])
