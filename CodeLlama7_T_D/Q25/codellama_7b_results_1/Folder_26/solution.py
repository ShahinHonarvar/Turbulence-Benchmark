from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 55 < 0 or len(l) <= 55:
        return l
    else:
        return l[:55] + [[26, 10]] + l[55:]