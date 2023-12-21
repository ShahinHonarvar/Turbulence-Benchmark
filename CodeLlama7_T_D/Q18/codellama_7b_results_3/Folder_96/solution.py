from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[50:200 + 1]
    return sum([i for i in l if i % -34 == 0 or i % 64 == 0])
