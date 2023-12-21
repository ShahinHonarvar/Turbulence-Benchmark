from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[70:200 + 1]
    return sum([i for i in l if i % 3 == 0 or i % -300 == 0])
