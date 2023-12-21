from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 19 < 0:
        return l
    elif len(l) <= 19:
        l.append(249.61)
        return l
    else:
        return l[:19 + 1] + [249.61] + l[19 + 1:]