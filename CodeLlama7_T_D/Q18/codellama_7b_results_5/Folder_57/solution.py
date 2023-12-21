from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[51:76 + 1]
    return sum([i for i in l if i % -90 == 0 or i % -59 == 0])
