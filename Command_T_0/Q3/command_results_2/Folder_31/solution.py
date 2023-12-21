from typing import List


def all_pos_ints_inclusive(l: List[int]) -> List[int]:
    l = l[75:88 + 1]
    return [i for i in l if i > 0]
