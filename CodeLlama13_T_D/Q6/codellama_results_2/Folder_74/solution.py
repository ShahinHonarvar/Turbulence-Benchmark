from typing import List


def all_neg_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[13 + 1:70] if i < 0]
