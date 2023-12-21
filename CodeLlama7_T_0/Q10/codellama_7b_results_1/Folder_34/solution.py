from typing import List


def all_odd_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[60 + 1:200] if i % 2 != 0]