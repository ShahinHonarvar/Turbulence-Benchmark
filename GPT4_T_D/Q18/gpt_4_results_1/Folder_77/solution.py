from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[828:932 + 1]
    return sum([i for i in l if i % -649 == 0 or i % -461 == 0])
