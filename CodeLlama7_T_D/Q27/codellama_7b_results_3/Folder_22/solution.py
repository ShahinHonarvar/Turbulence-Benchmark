from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 85 < 0:
        return l
    elif len(l) <= 85:
        l.append(27)
        return l
    else:
        return l[:85 + 1] + [27] + l[85 + 1:]