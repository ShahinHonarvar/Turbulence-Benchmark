from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 761 < 0:
        return l
    elif len(l) <= 761:
        l.append(925)
        return l
    else:
        return l[:761 + 1] + [925] + l[761 + 1:]