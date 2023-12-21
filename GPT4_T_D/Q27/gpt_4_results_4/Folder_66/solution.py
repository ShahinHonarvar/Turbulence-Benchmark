from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 62 < 0:
        return l
    elif len(l) <= 62:
        l.append([19, 13])
        return l
    else:
        return l[:62 + 1] + [[19, 13]] + l[62 + 1:]