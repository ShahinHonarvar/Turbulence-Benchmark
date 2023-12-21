from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[13:76 + 1]
    return sum([i for i in l if i % -66 == 0 or i % -32 == 0])
