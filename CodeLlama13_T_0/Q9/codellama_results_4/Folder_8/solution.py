from typing import List


def all_odd_ints_inclusive(l: List[int]) -> List[int]:
    return [i for i in l[23:23 + 1] if i % 2 != 0]