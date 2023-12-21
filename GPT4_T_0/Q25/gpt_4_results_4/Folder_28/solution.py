from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 74 < 0 or len(l) <= 74:
        return l
    else:
        return l[:74] + [49] + l[74:]