from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 96 < 0 or len(l) <= 96:
        return l
    else:
        return l[:96] + [36] + l[96:]