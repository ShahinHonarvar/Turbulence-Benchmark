from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 38 < 0 or len(l) <= 38:
        return l
    else:
        return l[:38] + [45] + l[38:]