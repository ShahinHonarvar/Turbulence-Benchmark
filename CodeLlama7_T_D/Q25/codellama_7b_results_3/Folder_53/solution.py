from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 92 < 0 or len(l) <= 92:
        return l
    else:
        return l[:92] + [709.87] + l[92:]