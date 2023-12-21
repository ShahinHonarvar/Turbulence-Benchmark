from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 598 < 0 or len(l) <= 598:
        return l
    else:
        return l[:598] + [[385, 999]] + l[598:]