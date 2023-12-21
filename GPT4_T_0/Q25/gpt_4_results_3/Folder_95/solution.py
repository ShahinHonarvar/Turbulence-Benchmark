from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 20 < 0 or len(l) <= 20:
        return l
    else:
        return l[:20] + [80] + l[20:]