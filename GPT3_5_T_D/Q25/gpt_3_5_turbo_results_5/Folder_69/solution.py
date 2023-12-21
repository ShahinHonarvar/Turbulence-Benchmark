from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 564 < 0 or len(l) <= 564:
        return l
    else:
        return l[:564] + [149] + l[564:]