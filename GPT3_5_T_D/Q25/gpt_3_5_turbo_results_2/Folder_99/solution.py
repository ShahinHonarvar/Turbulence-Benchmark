from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 295 < 0 or len(l) <= 295:
        return l
    else:
        return l[:295] + [[276, 376]] + l[295:]