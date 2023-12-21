from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 696 < 0 or len(l) <= 696:
        return l
    else:
        return l[:696] + [477] + l[696:]