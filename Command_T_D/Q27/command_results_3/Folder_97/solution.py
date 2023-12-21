from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 500 < 0:
        return l
    elif len(l) <= 500:
        l.append([912, 170])
        return l
    else:
        return l[:500 + 1] + [[912, 170]] + l[500 + 1:]