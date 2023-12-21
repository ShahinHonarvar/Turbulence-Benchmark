from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 49 < 0:
        return l
    elif len(l) <= 49:
        l.append(0.78)
        return l
    else:
        return l[:49 + 1] + [0.78] + l[49 + 1:]