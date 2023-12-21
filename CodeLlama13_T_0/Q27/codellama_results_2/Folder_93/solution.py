from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 36 < 0:
        return l
    elif len(l) <= 36:
        l.append([54, 13])
        return l
    else:
        return l[:36 + 1] + [[54, 13]] + l[36 + 1:]