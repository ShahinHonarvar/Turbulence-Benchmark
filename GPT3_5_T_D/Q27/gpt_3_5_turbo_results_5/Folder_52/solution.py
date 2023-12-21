from typing import List


def insert_after_index(l: List[object]) -> List[object]:
    if 97 < 0:
        return l
    elif len(l) <= 97:
        l.append(72.27)
        return l
    else:
        return l[:97 + 1] + [72.27] + l[97 + 1:]