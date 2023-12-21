from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[90:97 + 1]
    return sum([i for i in l if i % 13 == 0 or i % 35 == 0])
