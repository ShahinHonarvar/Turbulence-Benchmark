from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 564 < 0:
        return l
    elif len(l) <= 564:
        l.append(149)
        return l
    else:
        return l[:564 + 1] + [149] + l[564 + 1:]