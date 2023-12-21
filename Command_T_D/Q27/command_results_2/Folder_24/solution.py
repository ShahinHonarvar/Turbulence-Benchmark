from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 42 < 0:
        return l
    elif len(l) <= 42:
        l.append(53)
        return l
    else:
        return l[:42 + 1] + [53] + l[42 + 1:]