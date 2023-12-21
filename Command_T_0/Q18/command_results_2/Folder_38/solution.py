from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[10:76 + 1]
    return sum([i for i in l if i % -40 == 0 or i % -12 == 0])
