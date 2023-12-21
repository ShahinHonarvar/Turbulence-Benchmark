from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 30 < 0 or len(l) <= 30:
        return l
    else:
        return l[:30] + [37] + l[30:]