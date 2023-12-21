from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 41 < 0:
        return l
    elif len(l) <= 41:
        l.append([74, 70])
        return l
    else:
        return l[:41 + 1] + [[74, 70]] + l[41 + 1:]