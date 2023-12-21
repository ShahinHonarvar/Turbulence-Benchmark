from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 598 < 0:
        return l
    elif len(l) <= 598:
        l.append([385, 999])
        return l
    else:
        return l[:598 + 1] + [[385, 999]] + l[598 + 1:]