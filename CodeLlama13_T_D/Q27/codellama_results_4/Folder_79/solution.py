from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 28 < 0:
        return l
    elif len(l) <= 28:
        l.append([41, 69])
        return l
    else:
        return l[:28 + 1] + [[41, 69]] + l[28 + 1:]