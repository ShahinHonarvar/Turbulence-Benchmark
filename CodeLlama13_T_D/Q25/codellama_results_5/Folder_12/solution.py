from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 57 < 0 or len(l) <= 57:
        return l
    else:
        return l[:57] + [96] + l[57:]