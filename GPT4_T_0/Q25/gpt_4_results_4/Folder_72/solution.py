from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 24 < 0 or len(l) <= 24:
        return l
    else:
        return l[:24] + [[98, 22]] + l[24:]