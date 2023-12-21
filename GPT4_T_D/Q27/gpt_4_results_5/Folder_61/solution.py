from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 4 < 0:
        return l
    elif len(l) <= 4:
        l.append(7)
        return l
    else:
        return l[:4 + 1] + [7] + l[4 + 1:]