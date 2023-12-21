from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[25:95 + 1]
    return sum([i for i in l if i % 51 == 0 or i % 77 == 0])
