from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 8 < 0 or len(l) <= 8:
        return l
    else:
        return l[:8] + [[3, 8]] + l[8:]