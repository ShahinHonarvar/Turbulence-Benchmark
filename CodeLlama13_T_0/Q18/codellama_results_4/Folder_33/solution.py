from typing import List


def sum_ints_div_by_either_nums(l: List[int]) -> int:
    l = l[281:694 + 1]
    return sum([i for i in l if i % -722 == 0 or i % -731 == 0])
