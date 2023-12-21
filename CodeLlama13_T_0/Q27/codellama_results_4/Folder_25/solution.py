from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 30 < 0:
        return l
    elif len(l) <= 30:
        l.append(37)
        return l
    else:
        return l[:30 + 1] + [37] + l[30 + 1:]