from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[28:96 + 1]
    return sum([i for i in l if i % 90 == 0 or i % 97 == 0])
