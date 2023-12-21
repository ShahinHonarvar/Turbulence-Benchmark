from typing import List


def all_odd_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[11 + 1:76] if i % 2 != 0]