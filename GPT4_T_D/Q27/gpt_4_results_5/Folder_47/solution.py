from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 64 < 0:
        return l
    elif len(l) <= 64:
        l.append(520.11)
        return l
    else:
        return l[:64 + 1] + [520.11] + l[64 + 1:]