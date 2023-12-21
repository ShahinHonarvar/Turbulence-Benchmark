from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 500 < 0 or len(l) <= 500:
        return l
    else:
        return l[:500] + [[912, 170]] + l[500:]