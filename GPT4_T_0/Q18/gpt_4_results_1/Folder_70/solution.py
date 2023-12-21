from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[42:43 + 1]
    return sum([i for i in l if i % 15 == 0 or i % 87 == 0])
