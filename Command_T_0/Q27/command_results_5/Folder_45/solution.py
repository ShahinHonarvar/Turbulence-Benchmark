from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 84 < 0:
        return l
    elif len(l) <= 84:
        l.append([13, 46])
        return l
    else:
        return l[:84 + 1] + [[13, 46]] + l[84 + 1:]