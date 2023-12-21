from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 32 < 0:
        return l
    elif len(l) <= 32:
        l.append([54, 96])
        return l
    else:
        return l[:32 + 1] + [[54, 96]] + l[32 + 1:]