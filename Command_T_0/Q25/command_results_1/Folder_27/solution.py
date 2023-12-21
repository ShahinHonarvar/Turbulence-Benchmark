from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 85 < 0 or len(l) <= 85:
        return l
    else:
        return l[:85] + [[41, 95]] + l[85:]