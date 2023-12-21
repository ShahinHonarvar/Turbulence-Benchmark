from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[68:99 + 1]
    return sum([i for i in l if i % -37 == 0 or i % -26 == 0])
