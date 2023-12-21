from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 43 < 0 or len(l) <= 43:
        return l
    else:
        return l[:43] + [37] + l[43:]