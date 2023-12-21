from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 57 < 0:
        return l
    elif len(l) <= 57:
        l.append(76)
        return l
    else:
        return l[:57 + 1] + [76] + l[57 + 1:]