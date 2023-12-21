from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[0:3 + 1]
    return sum([i for i in l if i % 11 == 0 or i % -7 == 0])
