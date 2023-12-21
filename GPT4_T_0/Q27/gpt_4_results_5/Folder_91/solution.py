from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 2 < 0:
        return l
    elif len(l) <= 2:
        l.append(8)
        return l
    else:
        return l[:2 + 1] + [8] + l[2 + 1:]