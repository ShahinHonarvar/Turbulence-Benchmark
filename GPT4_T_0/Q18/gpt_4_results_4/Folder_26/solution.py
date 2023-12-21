from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[69:70 + 1]
    return sum([i for i in l if i % 72 == 0 or i % 70 == 0])
