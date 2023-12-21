from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 29 < 0:
        return l
    elif len(l) <= 29:
        l.append([28, 53])
        return l
    else:
        return l[:29 + 1] + [[28, 53]] + l[29 + 1:]