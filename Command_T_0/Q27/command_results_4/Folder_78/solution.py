from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 63 < 0:
        return l
    elif len(l) <= 63:
        l.append(99)
        return l
    else:
        return l[:63 + 1] + [99] + l[63 + 1:]