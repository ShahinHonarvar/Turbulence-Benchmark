from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[56:88 + 1]
    return sum([i for i in l if i % -59 == 0 or i % -79 == 0])
