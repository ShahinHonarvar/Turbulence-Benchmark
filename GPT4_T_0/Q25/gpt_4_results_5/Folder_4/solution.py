from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 60 < 0 or len(l) <= 60:
        return l
    else:
        return l[:60] + [[80, 74]] + l[60:]