from typing import List


def all_neg_ints_inclusive(l: List[int]) -> List[int]:
    return [i for i in l[310:370 + 1] if i < 0]
