from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 48 < 0 or len(l) <= 48:
        return l
    else:
        return l[:48] + [[86, 77]] + l[48:]