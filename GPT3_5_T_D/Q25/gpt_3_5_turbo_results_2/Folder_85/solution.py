from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 51 < 0 or len(l) <= 51:
        return l
    else:
        return l[:51] + [304.62] + l[51:]