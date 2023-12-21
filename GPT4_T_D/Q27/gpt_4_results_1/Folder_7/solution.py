from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 323 < 0:
        return l
    elif len(l) <= 323:
        l.append([389, 303])
        return l
    else:
        return l[:323 + 1] + [[389, 303]] + l[323 + 1:]