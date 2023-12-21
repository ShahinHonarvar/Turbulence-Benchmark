from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 97 < 0:
        return l
    elif len(l) <= 97:
        l.append([47, 22])
        return l
    else:
        return l[:97 + 1] + [[47, 22]] + l[97 + 1:]