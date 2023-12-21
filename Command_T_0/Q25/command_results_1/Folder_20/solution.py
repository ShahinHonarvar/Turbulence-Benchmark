from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 32 < 0 or len(l) <= 32:
        return l
    else:
        return l[:32] + [[54, 96]] + l[32:]