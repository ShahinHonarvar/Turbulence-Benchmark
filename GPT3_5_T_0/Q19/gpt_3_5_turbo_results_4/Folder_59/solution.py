from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[8 + 1:9]
    return [i for i in l if i % 8 != 0]
