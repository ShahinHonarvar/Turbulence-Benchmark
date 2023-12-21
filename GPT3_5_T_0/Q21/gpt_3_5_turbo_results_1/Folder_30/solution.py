from typing import List


def all_ints_div_by_num(l: List[int]) -> List[int]:
    l = l[59:79 + 1]
    return [i for i in l if i % -82 == 0]
