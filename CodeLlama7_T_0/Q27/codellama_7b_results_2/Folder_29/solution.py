from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 96 < 0:
        return l
    elif len(l) <= 96:
        l.append(36)
        return l
    else:
        return l[:96 + 1] + [36] + l[96 + 1:]