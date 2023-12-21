from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 100 < 0:
        return l
    elif len(l) <= 100:
        l.append([876, 203])
        return l
    else:
        return l[:100 + 1] + [[876, 203]] + l[100 + 1:]