from typing import List


def all_neg_ints_inclusive(l: List[int]) -> List[int]:
    return [i for i in l[64:66 + 1] if i < 0]
