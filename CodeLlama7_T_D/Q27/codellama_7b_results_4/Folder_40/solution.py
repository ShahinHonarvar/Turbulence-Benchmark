from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 4 < 0:
        return l
    elif len(l) <= 4:
        l.append(856.69)
        return l
    else:
        return l[:4 + 1] + [856.69] + l[4 + 1:]