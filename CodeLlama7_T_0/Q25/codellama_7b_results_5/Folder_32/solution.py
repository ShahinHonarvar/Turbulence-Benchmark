from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 76 < 0 or len(l) <= 76:
        return l
    else:
        return l[:76] + [10.01] + l[76:]