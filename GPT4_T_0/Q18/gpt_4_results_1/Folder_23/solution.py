from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[69:97 + 1]
    return sum([i for i in l if i % -90 == 0 or i % -67 == 0])
