from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 40 < 0 or len(l) <= 40:
        return l
    else:
        return l[:40] + [169.26] + l[40:]