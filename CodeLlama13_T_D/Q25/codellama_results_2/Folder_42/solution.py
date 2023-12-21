from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 44 < 0 or len(l) <= 44:
        return l
    else:
        return l[:44] + [[40, 27]] + l[44:]