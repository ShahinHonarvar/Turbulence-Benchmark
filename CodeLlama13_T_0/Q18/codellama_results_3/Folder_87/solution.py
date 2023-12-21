from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[18:52 + 1]
    return sum([i for i in l if i % 15 == 0 or i % 57 == 0])
