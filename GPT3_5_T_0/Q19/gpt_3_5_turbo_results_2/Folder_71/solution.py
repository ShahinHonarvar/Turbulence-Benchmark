from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[21 + 1:51]
    return [i for i in l if i % -77 != 0]
