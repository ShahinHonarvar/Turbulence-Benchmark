from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 370 < 0:
        return l
    elif len(l) <= 370:
        l.append(285.4)
        return l
    else:
        return l[:370 + 1] + [285.4] + l[370 + 1:]