from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[58:81 + 1]
    return sum([i for i in l if i % 55 == 0 or i % 10 == 0])
