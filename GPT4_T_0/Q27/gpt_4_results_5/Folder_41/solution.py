from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 87 < 0:
        return l
    elif len(l) <= 87:
        l.append([78, 16])
        return l
    else:
        return l[:87 + 1] + [[78, 16]] + l[87 + 1:]