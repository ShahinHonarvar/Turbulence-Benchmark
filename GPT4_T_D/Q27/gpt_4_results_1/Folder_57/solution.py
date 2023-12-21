from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 90 < 0:
        return l
    elif len(l) <= 90:
        l.append(80)
        return l
    else:
        return l[:90 + 1] + [80] + l[90 + 1:]