from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 56 < 0 or len(l) <= 56:
        return l
    else:
        return l[:56] + [54] + l[56:]