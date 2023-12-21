from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 370 < 0 or len(l) <= 370:
        return l
    else:
        return l[:370] + [285.4] + l[370:]