from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[86:90 + 1]
    return sum([i for i in l if i % -71 == 0 or i % -67 == 0])
