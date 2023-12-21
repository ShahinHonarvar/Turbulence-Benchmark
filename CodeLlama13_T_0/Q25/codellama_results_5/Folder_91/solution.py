from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 2 < 0 or len(l) <= 2:
        return l
    else:
        return l[:2] + [8] + l[2:]