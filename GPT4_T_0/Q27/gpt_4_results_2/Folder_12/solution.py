from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 57 < 0:
        return l
    elif len(l) <= 57:
        l.append(96)
        return l
    else:
        return l[:57 + 1] + [96] + l[57 + 1:]