from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 295 < 0:
        return l
    elif len(l) <= 295:
        l.append([276, 376])
        return l
    else:
        return l[:295 + 1] + [[276, 376]] + l[295 + 1:]