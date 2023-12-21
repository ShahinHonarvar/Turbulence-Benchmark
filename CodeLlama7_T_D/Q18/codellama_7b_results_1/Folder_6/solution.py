from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[41:56 + 1]
    return sum([i for i in l if i % 82 == 0 or i % 90 == 0])
