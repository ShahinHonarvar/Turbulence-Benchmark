from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 585 < 0:
        return l
    elif len(l) <= 585:
        l.append(993.71)
        return l
    else:
        return l[:585 + 1] + [993.71] + l[585 + 1:]