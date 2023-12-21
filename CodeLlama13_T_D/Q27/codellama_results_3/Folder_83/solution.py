from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 13 < 0:
        return l
    elif len(l) <= 13:
        l.append([56, 54])
        return l
    else:
        return l[:13 + 1] + [[56, 54]] + l[13 + 1:]