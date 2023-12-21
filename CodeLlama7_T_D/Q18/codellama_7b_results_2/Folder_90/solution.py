from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[138:424 + 1]
    return sum([i for i in l if i % -863 == 0 or i % -329 == 0])
