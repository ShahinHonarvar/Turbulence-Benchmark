from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 21 < 0 or len(l) <= 21:
        return l
    else:
        return l[:21] + [655.24] + l[21:]