from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 29 < 0 or len(l) <= 29:
        return l
    else:
        return l[:29] + [[28, 53]] + l[29:]