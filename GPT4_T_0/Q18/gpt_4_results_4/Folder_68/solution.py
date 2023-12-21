from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[7:7 + 1]
    return sum([i for i in l if i % 5 == 0 or i % 7 == 0])
