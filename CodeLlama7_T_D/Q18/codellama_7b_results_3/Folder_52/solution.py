from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[48:59 + 1]
    return sum([i for i in l if i % 88 == 0 or i % 58 == 0])
