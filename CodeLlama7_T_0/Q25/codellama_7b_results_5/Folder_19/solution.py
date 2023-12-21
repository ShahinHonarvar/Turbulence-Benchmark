from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 49 < 0 or len(l) <= 49:
        return l
    else:
        return l[:49] + [0.78] + l[49:]