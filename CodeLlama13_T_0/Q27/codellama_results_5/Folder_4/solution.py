from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 60 < 0:
        return l
    elif len(l) <= 60:
        l.append([80, 74])
        return l
    else:
        return l[:60 + 1] + [[80, 74]] + l[60 + 1:]