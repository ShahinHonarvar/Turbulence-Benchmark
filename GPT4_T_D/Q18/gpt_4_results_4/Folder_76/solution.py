from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[250:629 + 1]
    return sum([i for i in l if i % 850 == 0 or i % 587 == 0])
