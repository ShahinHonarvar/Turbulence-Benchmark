from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 90 < 0 or len(l) <= 90:
        return l
    else:
        return l[:90] + [80] + l[90:]