from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 93 < 0 or len(l) <= 93:
        return l
    else:
        return l[:93] + [[33, 78]] + l[93:]