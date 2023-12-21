from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 166 < 0:
        return l
    elif len(l) <= 166:
        l.append(232)
        return l
    else:
        return l[:166 + 1] + [232] + l[166 + 1:]