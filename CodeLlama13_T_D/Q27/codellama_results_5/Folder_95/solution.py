from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 20 < 0:
        return l
    elif len(l) <= 20:
        l.append(80)
        return l
    else:
        return l[:20 + 1] + [80] + l[20 + 1:]