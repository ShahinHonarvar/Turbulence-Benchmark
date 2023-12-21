from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 31 < 0:
        return l
    elif len(l) <= 31:
        l.append([88, 51])
        return l
    else:
        return l[:31 + 1] + [[88, 51]] + l[31 + 1:]