from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 56 < 0:
        return l
    elif len(l) <= 56:
        l.append(54)
        return l
    else:
        return l[:56 + 1] + [54] + l[56 + 1:]