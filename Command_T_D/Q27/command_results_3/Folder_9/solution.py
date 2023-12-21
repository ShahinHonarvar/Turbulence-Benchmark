from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 66 < 0:
        return l
    elif len(l) <= 66:
        l.append(45)
        return l
    else:
        return l[:66 + 1] + [45] + l[66 + 1:]