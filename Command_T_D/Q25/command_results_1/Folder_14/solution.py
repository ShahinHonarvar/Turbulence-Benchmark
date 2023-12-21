from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 15 < 0 or len(l) <= 15:
        return l
    else:
        return l[:15] + [550.97] + l[15:]