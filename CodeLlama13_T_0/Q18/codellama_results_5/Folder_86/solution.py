from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[54:79 + 1]
    return sum([i for i in l if i % 54 == 0 or i % 28 == 0])
