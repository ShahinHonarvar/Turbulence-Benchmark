from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 53 < 0:
        return l
    elif len(l) <= 53:
        l.append(783.25)
        return l
    else:
        return l[:53 + 1] + [783.25] + l[53 + 1:]