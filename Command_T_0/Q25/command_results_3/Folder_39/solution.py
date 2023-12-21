from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 97 < 0 or len(l) <= 97:
        return l
    else:
        return l[:97] + [[47, 22]] + l[97:]