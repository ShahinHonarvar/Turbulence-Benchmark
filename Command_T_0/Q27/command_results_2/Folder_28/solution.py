from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 74 < 0:
        return l
    elif len(l) <= 74:
        l.append(49)
        return l
    else:
        return l[:74 + 1] + [49] + l[74 + 1:]