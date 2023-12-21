from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 9 < 0:
        return l
    elif len(l) <= 9:
        l.append(426.08)
        return l
    else:
        return l[:9 + 1] + [426.08] + l[9 + 1:]