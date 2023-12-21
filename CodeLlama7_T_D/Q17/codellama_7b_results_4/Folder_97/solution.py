from typing import List


def all_ints_div_by_both_two_nums(l: List[int]) -> List[int]:
    l = l[58:75 + 1]
    return [i for i in l if i % 72 == 0 and i % 62 == 0]
