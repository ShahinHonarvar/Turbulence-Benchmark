from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[50:92 + 1]
    return sum([i for i in l if i % -94 == 0 or i % -95 == 0])
