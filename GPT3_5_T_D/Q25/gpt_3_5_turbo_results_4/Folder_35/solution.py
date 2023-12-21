from typing import List


def insert_at_index(l: List[object]) -> List[object]:
    if 100 < 0 or len(l) <= 100:
        return l
    else:
        return l[:100] + [[876, 203]] + l[100:]