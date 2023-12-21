from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 52 < 0:
        return l
    elif len(l) <= 52:
        l.append(38)
        return l
    else:
        return l[:52 + 1] + [38] + l[52 + 1:]