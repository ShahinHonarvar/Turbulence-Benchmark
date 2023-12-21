from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 99 < 0 or len(l) <= 99:
        return l
    else:
        return l[:99] + [15] + l[99:]