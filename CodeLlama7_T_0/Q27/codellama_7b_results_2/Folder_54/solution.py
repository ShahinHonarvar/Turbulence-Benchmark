from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 43 < 0:
        return l
    elif len(l) <= 43:
        l.append(37)
        return l
    else:
        return l[:43 + 1] + [37] + l[43 + 1:]