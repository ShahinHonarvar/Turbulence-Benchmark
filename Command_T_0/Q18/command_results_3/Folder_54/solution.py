from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[13:91 + 1]
    return sum([i for i in l if i % -65 == 0 or i % -62 == 0])
