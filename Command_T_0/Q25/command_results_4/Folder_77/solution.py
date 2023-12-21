from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 585 < 0 or len(l) <= 585:
        return l
    else:
        return l[:585] + [993.71] + l[585:]