from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 76 < 0:
        return l
    elif len(l) <= 76:
        l.append([15, 51])
        return l
    else:
        return l[:76 + 1] + [[15, 51]] + l[76 + 1:]