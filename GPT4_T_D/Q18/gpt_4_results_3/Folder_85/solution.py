from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[1:8 + 1]
    return sum([i for i in l if i % -9 == 0 or i % -3 == 0])
