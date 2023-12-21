from typing import List


def sum_even_ints_inclusive(l: List[int]) -> int:
    l = l[4:8 + 1]
    return sum([i for i in l if i % 2 == 0])