from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[90:200 + 1]
    return sum([i for i in l if i % -31 == 0 or i % 13 == 0])
