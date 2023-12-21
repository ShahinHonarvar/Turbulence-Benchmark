from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[14:93 + 1]
    return sum([i for i in l if i % 71 == 0 or i % 81 == 0])
