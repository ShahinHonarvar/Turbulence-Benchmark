from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[61:88 + 1]
    return sum([i for i in l if i % 31 == 0 or i % 11 == 0])
