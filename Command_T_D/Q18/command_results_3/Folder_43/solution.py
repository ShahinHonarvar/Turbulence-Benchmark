from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[57:85 + 1]
    return sum([i for i in l if i % -77 == 0 or i % -32 == 0])
