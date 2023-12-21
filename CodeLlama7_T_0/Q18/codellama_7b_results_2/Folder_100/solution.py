from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[72:93 + 1]
    return sum([i for i in l if i % 32 == 0 or i % 44 == 0])
