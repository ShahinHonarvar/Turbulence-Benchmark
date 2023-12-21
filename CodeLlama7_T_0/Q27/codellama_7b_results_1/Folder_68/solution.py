from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 7 < 0:
        return l
    elif len(l) <= 7:
        l.append([1, 7])
        return l
    else:
        return l[:7 + 1] + [[1, 7]] + l[7 + 1:]