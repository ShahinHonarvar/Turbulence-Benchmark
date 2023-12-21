from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 0 < 0:
        return l
    elif len(l) <= 0:
        l.append(0)
        return l
    else:
        return l[:0 + 1] + [0] + l[0 + 1:]