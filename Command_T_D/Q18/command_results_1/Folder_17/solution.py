from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[81:89 + 1]
    return sum([i for i in l if i % 56 == 0 or i % 68 == 0])
