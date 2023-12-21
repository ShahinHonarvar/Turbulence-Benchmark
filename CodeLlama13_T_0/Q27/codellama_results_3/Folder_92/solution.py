from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 1 < 0:
        return l
    elif len(l) <= 1:
        l.append(478.12)
        return l
    else:
        return l[:1 + 1] + [478.12] + l[1 + 1:]