from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 41 < 0 or len(l) <= 41:
        return l
    else:
        return l[:41] + [[74, 70]] + l[41:]