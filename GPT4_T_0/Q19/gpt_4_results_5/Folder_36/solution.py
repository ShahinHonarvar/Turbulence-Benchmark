from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[472 + 1:827]
    return [i for i in l if i % 602 != 0]
