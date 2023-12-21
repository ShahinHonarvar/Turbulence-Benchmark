from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 7 < 0 or len(l) <= 7:
        return l
    else:
        return l[:7] + [[1, 7]] + l[7:]