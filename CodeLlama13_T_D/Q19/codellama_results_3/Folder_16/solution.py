from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[24 + 1:32]
    return [i for i in l if i % 35 != 0]
