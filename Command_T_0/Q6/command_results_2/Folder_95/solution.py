from typing import List


def all_neg_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[25 + 1:80] if i < 0]
