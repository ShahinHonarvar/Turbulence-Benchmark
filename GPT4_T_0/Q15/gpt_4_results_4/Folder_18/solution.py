from typing import List


def sum_odd_ints_inclusive(l: List[int]) -> int:
    l = l[35:49 + 1]
    return sum([i for i in l if i % 2 != 0])