from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 40 < 0:
        return l
    elif len(l) <= 40:
        l.append(169.26)
        return l
    else:
        return l[:40 + 1] + [169.26] + l[40 + 1:]