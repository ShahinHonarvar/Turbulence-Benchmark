from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 8 < 0:
        return l
    elif len(l) <= 8:
        l.append([3, 8])
        return l
    else:
        return l[:8 + 1] + [[3, 8]] + l[8 + 1:]