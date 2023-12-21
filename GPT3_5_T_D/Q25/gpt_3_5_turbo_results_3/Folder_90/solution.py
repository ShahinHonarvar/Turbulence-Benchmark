from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 761 < 0 or len(l) <= 761:
        return l
    else:
        return l[:761] + [925] + l[761:]