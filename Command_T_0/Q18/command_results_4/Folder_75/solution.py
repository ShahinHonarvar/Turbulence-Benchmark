from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[20:93 + 1]
    return sum([i for i in l if i % -92 == 0 or i % -50 == 0])
