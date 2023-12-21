from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[81:86 + 1]
    return sum([i for i in l if i % -33 == 0 or i % -62 == 0])
