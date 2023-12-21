from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 44 < 0:
        return l
    elif len(l) <= 44:
        l.append(76)
        return l
    else:
        return l[:44 + 1] + [76] + l[44 + 1:]