from typing import List


def sum_in_range(l: List[int]) -> int:
    return sum([i for i in l if 1 <= i <= 7])
