from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 51 < 0:
        return l
    elif len(l) <= 51:
        l.append(304.62)
        return l
    else:
        return l[:51 + 1] + [304.62] + l[51 + 1:]