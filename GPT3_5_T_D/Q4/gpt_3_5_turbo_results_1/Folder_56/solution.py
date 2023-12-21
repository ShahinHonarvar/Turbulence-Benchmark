from typing import List


def all_pos_ints_exclusive(l: List[int]) -> List[int]:
    return [i for i in l[7 + 1:9] if i > 0]
