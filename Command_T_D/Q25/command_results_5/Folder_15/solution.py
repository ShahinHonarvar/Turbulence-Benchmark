from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 0 < 0 or len(l) <= 0:
        return l
    else:
        return l[:0] + [0] + l[0:]