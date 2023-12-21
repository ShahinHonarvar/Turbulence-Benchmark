from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 4 < 0 or len(l) <= 4:
        return l
    else:
        return l[:4] + [7] + l[4:]