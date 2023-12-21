from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[240:901 + 1]
    return sum([i for i in l if i % 546 == 0 or i % 709 == 0])
