from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 38 < 0:
        return l
    elif len(l) <= 38:
        l.append(45)
        return l
    else:
        return l[:38 + 1] + [45] + l[38 + 1:]