from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[20:35 + 1]
    return sum([i for i in l if i % -36 == 0 or i % -89 == 0])
