from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 53 < 0 or len(l) <= 53:
        return l
    else:
        return l[:53] + [783.25] + l[53:]