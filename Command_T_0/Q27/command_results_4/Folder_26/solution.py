from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 55 < 0:
        return l
    elif len(l) <= 55:
        l.append([26, 10])
        return l
    else:
        return l[:55 + 1] + [[26, 10]] + l[55 + 1:]