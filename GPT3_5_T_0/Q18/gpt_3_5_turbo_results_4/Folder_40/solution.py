from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[0:1 + 1]
    return sum([i for i in l if i % 2 == 0 or i % 1 == 0])
