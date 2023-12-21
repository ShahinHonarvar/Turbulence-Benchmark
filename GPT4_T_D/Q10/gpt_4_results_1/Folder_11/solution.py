from typing import List


def all_odd_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[15 + 1:99] if i % 2 != 0]