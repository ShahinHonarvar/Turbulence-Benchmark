from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 63 < 0 or len(l) <= 63:
        return l
    else:
        return l[:63] + [99] + l[63:]