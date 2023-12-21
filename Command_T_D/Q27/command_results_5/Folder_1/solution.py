from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 93 < 0:
        return l
    elif len(l) <= 93:
        l.append([33, 78])
        return l
    else:
        return l[:93 + 1] + [[33, 78]] + l[93 + 1:]