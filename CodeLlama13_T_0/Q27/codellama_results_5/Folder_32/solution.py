from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 76 < 0:
        return l
    elif len(l) <= 76:
        l.append(10.01)
        return l
    else:
        return l[:76 + 1] + [10.01] + l[76 + 1:]