from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 28 < 0 or len(l) <= 28:
        return l
    else:
        return l[:28] + [[41, 69]] + l[28:]