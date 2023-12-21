from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 36 < 0 or len(l) <= 36:
        return l
    else:
        return l[:36] + [[54, 13]] + l[36:]