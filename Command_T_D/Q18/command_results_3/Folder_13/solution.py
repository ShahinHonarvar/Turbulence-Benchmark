from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[13:18 + 1]
    return sum([i for i in l if i % 45 == 0 or i % 20 == 0])
