from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 743 < 0:
        return l
    elif len(l) <= 743:
        l.append(11.04)
        return l
    else:
        return l[:743 + 1] + [11.04] + l[743 + 1:]