from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 86 < 0 or len(l) <= 86:
        return l
    else:
        return l[:86] + [581.49] + l[86:]