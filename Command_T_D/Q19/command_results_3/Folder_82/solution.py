from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[20 + 1:200]
    return [i for i in l if i % -200 != 0]
