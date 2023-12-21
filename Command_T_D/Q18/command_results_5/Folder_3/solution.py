from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[38:52 + 1]
    return sum([i for i in l if i % -41 == 0 or i % -47 == 0])
