from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[543:584 + 1]
    return sum([i for i in l if i % -553 == 0 or i % -737 == 0])
