from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 99 < 0:
        return l
    elif len(l) <= 99:
        l.append(99)
        return l
    else:
        return l[:99 + 1] + [99] + l[99 + 1:]