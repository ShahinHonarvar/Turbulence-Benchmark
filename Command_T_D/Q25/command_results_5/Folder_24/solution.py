from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 42 < 0 or len(l) <= 42:
        return l
    else:
        return l[:42] + [53] + l[42:]