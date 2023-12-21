from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 743 < 0 or len(l) <= 743:
        return l
    else:
        return l[:743] + [11.04] + l[743:]