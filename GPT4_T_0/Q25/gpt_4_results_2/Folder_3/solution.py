from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 31 < 0 or len(l) <= 31:
        return l
    else:
        return l[:31] + [[88, 51]] + l[31:]