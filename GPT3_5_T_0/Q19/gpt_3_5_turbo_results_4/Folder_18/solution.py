from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[35 + 1:98]
    return [i for i in l if i % 41 != 0]
