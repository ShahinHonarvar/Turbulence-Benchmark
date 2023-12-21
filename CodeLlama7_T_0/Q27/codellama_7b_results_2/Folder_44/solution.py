from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 48 < 0:
        return l
    elif len(l) <= 48:
        l.append([86, 77])
        return l
    else:
        return l[:48 + 1] + [[86, 77]] + l[48 + 1:]