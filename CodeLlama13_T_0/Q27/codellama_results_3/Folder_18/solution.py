from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 696 < 0:
        return l
    elif len(l) <= 696:
        l.append(477)
        return l
    else:
        return l[:696 + 1] + [477] + l[696 + 1:]