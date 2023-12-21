from typing import List


def all_odd_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[598 + 1:767] if i % 2 != 0]