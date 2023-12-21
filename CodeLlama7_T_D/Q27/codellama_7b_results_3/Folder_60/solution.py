from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 21 < 0:
        return l
    elif len(l) <= 21:
        l.append(74)
        return l
    else:
        return l[:21 + 1] + [74] + l[21 + 1:]