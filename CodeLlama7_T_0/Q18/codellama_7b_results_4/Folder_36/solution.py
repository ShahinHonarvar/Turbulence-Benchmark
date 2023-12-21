from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[299:382 + 1]
    return sum([i for i in l if i % 858 == 0 or i % 952 == 0])
