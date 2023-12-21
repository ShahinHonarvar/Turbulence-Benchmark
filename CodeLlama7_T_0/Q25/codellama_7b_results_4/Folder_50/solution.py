from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 52 < 0 or len(l) <= 52:
        return l
    else:
        return l[:52] + [38] + l[52:]