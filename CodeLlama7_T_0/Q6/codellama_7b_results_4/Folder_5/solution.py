from typing import List


def all_neg_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[2 + 1:7] if i < 0]
