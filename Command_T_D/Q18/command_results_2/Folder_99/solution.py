from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[154:798 + 1]
    return sum([i for i in l if i % 275 == 0 or i % 580 == 0])
