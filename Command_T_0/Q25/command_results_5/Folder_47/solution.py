from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 64 < 0 or len(l) <= 64:
        return l
    else:
        return l[:64] + [520.11] + l[64:]