from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[10:79 + 1]
    return sum([i for i in l if i % -74 == 0 or i % -58 == 0])
