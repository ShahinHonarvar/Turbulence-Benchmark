from typing import List


def all_ints_not_div_by_num(l: List[int]) -> List[int]:
    l = l[19 + 1:69]
    return [i for i in l if i % 97 != 0]
