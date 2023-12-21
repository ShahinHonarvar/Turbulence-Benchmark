from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[29:45 + 1]
    return sum([i for i in l if i % 27 == 0 or i % 81 == 0])
